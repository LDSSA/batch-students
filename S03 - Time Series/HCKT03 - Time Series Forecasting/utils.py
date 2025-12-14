import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
#from lightgbm import LGBMRegressor
from tqdm import tqdm_notebook as tqdm

def load_airlines_series():
    airlines = pd.read_csv('data/AirPassengers.csv')
    airlines.Month = pd.to_datetime(airlines.Month)
    airlines = airlines.set_index('Month').sort_index()
    airlines.columns = ['thousands of passengers']
    return airlines['thousands of passengers'] # we want a series, not df

def get_store_one_data():
    stores = pd.read_csv('data/stores.csv')
    store = stores.loc[stores.store_nbr==1].drop('store_nbr', axis=1)
    store['date'] = pd.to_datetime(store['date'], format='%Y-%m-%d')
    store = store.set_index('date').sort_index()
    return store

def build_target(df, original, num_periods_ahead=1, target='target'):
    """ 
    Adds a target to df by shifting the original data from the future.
    """
    df_ = df.copy()
    df_[target] = original.shift(-num_periods_ahead)
    return df_
    
def build_lagged_features(df, original, num_lags): 
    """
    Adds new features to df from lags of the original time series.
    """
    df_ = df.copy()
    for i in range(1, num_lags+1):
        df_['lag_%s' % str(i)] = original.shift(i)      
    return df_

def build_diffed_features(df, original, num_diffs): 
    """
    Adds new features to df from diffs of the original time series.
    """
    df_ = df.copy()
    for i in range(1, num_diffs+1):
        df_['diff_%s' % str(i)] = original.diff(i)
    return df_

def build_rolling_features(df, original, rolling=[], rolling_freq='7D'):
    """
    Adds new features to df from rolling window statistics
    such as max, min, mean, std.
    """
    df_ = df.copy()
    for stat in rolling:
        df_['rolling_%s'%str(stat)] = original.rolling(rolling_freq).aggregate(stat)
    return df_

def build_holiday_features(df, holidays=False):
    """
    Builds holidays categorical feature.
    """
    df_ = df.copy()
    if holidays:
        holidays = (((df_.index.month==12) & (df_.index.day==25))
              |((df_.index.month==1) & (df_.index.day==1))) + 0 # +0 to convert bool to int
        df_['holidays'] = pd.Series(holidays, index=df_.index)
    return df_

def build_cyclical_features(df, weekday=False, month=False):
    """
    Build cyclical weekday and month features.
    """
    df_ = df.copy()
    if weekday == True:
        df_['sin_weekday'] = np.sin(2*np.pi*df_.index.weekday/7)
        df_['cos_weekday'] = np.cos(2*np.pi*df_.index.weekday/7)      
    if month == True:
        df_['sin_month'] = np.sin(2*np.pi*df_.index.month/12)
        df_['cos_month'] = np.cos(2*np.pi*df_.index.month/12)
    return df_    

def build_features(df, original, num_periods_ahead=1, num_lags=1, num_diffs=0, weekday=False, month=False,
                   rolling=[], rolling_freq='7D', holidays=False, exog=None, num_exog_lags=0, num_exog_diffs=0, num_exog_leads=0): 
    """
    Builds features for time series regression.
    """
    df_ = df.copy()
    df_ = build_lagged_features(df_, original, num_lags)
    df_ = build_diffed_features(df_, original, num_diffs)
    df_ = build_rolling_features(df_, original, rolling, rolling_freq)
    df_ = build_cyclical_features(df_, weekday, month)
    df_ = build_holiday_features(df_, holidays)
    df_ = build_exog_features(df_, exog=exog, num_periods_ahead=num_periods_ahead,
                              num_exog_lags=num_exog_lags, num_exog_diffs=num_exog_diffs, num_exog_leads=num_exog_leads)
    return df_

def prepare_train_set(df, target='target'): 
    """ 
    Separates the last period from the train set,
    drops null values, and prepares the features and the target for the model.
    """
    # anything that isn't a target is a feature
    features = [col for col in df.columns if col != target]
    last_period = df.iloc[-1:][features]
    train = df.iloc[:-1].dropna()
    X_train = train[features]
    y_train = train[target]
    return X_train, y_train, last_period

def prepare_data_for_modeling(original, num_lags=1, num_diffs=0, weekday=False, month=False,
                              rolling=[], rolling_freq='7D', holidays=False,
                              num_periods_ahead=1, target='target', exog=None, num_exog_lags=0, num_exog_diffs=0, num_exog_leads=0):
    """ 
    Prepare data for modeling.
    """
    df_ = pd.DataFrame(original)
    df_ = build_features(df_, original, num_periods_ahead=num_periods_ahead, num_lags=num_lags, 
                         num_diffs=num_diffs, weekday=weekday, month=month,
                         rolling=rolling, rolling_freq=rolling_freq, holidays=holidays,
                         exog=exog, num_exog_lags=num_exog_lags, num_exog_diffs=num_exog_diffs, num_exog_leads=num_exog_leads)
    df_ = build_target(df_, original, num_periods_ahead=num_periods_ahead, target=target)
    X_train, y_train, last_period = prepare_train_set(df_, target=target)
    return X_train, y_train, last_period

def forecast_period_n(original, model, num_lags=1, num_diffs=0, weekday=False, month=False,
                              rolling=[], rolling_freq='7D', holidays=False,
                              num_periods_ahead=1, target='target', exog=None, num_exog_lags=0, num_exog_diffs=0, num_exog_leads=0):
    """
    One-step forecast for n periods ahead.
    """
    X_train, y_train, last_period = prepare_data_for_modeling(original, num_lags=num_lags, num_diffs=num_diffs,
                                        weekday=weekday, month=month,rolling=rolling, rolling_freq=rolling_freq,
                                        holidays=holidays, num_periods_ahead=num_periods_ahead, target=target, exog=exog,               
                                        num_exog_lags=num_exog_lags, num_exog_diffs=num_exog_diffs, num_exog_leads=num_exog_leads)
    model.fit(X_train, y_train)
    return model.predict(last_period)[0]

def multistep_forecast(original, model, num_lags=1, num_diffs=0, weekday=False, month=False,
                              rolling=[], rolling_freq='7D', holidays=False,
                              num_periods_ahead=1, target='target', exog=None, num_exog_lags=0, num_exog_diffs=0,  num_exog_leads=0): 
    """
    Multi-step forecast for 1 to n periods ahead.
    """
    forecast = []
    for period_ahead in range(1, num_periods_ahead+1):
        pred = forecast_period_n(original=original, 
                                 model=model,
                                 num_lags=num_lags,
                                 num_diffs=num_diffs,
                                 weekday=weekday,
                                 month=month,
                                 rolling=rolling,
                                 rolling_freq=rolling_freq,
                                 holidays=holidays,
                                 num_periods_ahead=period_ahead,
                                 target=target,
                                 exog=exog,
                                 num_exog_lags=num_exog_lags,
                                 num_exog_diffs=num_exog_diffs,
                                 num_exog_leads=num_exog_leads)
        forecast.append(pred) 
    return forecast

def load_solar_data():
    df = pd.read_csv('data/pv.csv')
    df.Datetime = pd.to_datetime(df.Datetime)
    df = df.set_index('Datetime')
    df = df.sort_index()
    return df.asfreq('h')

def load_solar_radiation_data():
    exog = pd.read_csv('data/radiation.csv')
    exog.Datetime = pd.to_datetime(exog.Datetime)
    exog = exog.set_index('Datetime')
    exog = exog.sort_index()
    return exog.asfreq('h')

def build_exog_features(df, exog, num_periods_ahead=1, num_exog_lags=0, num_exog_diffs=0, num_exog_leads=0):
    """ 
    Adds the exogenous feature and the specified number of lags, diffs, and leads.
    """
    df_=df.copy()
    if exog is not None:
        df_['exog']=exog.shift(-num_periods_ahead).loc[df_.index]
        # Note that the lags, diffs, and leads are calculated from the shifted exog.
        for i in np.arange(1, num_exog_lags+1):
            df_['exog_lag_'+str(i)] = exog.shift(i-num_periods_ahead)
        for i in np.arange(1, num_exog_diffs+1):
            df_['exog_diff_'+str(i)] = exog.diff(-i-num_periods_ahead)
        for i in np.arange(1, num_exog_leads+1):
            df_['exog_lead_'+str(i)] = exog.shift(-i-num_periods_ahead)    
    return df_

def explain_linear_regression(lr, features):
    """
    Prints the equation of the linear regression with feature names and coefficient values
    """
    beta_0 = lr.intercept_
    betas = lr.coef_
    print('Regression: \n%0.3f' % beta_0)
    for b,f in zip(betas, features): 
        print('+ %0.3f * %s' % (b, f))

def load_electricity_consumption_series():
    data = pd.read_csv('data/monthly-av-residential-electrici.csv')
    data = data[:-1]
    data.Month = pd.to_datetime(data.Month)
    data.columns = ['month', 'consumption']
    data = data.set_index('month').sort_index()
    return data
