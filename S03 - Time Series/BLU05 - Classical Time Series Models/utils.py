import pandas as pd
import numpy as np
from random import gauss
from random import seed
seed(1)

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def load_airlines_series():
    airlines = pd.read_csv('data/AirPassengers.csv')
    airlines.Month = pd.to_datetime(airlines.Month)
    airlines = airlines.set_index('Month').sort_index()
    airlines.columns = ['thousands of passengers']
    return airlines['thousands of passengers'] # we want a series, not df

def load_electricity_consumption_series():
    data = pd.read_csv('data/monthly-av-residential-electrici.csv')
    data = data[:-1]
    data.Month = pd.to_datetime(data.Month)
    data.columns = ['month', 'consumption']
    data = data.set_index('month').sort_index()
    return data

def load_mysterious_data():
    mysterious_data_1 = load_electricity_consumption_series()['consumption']
    mysterious_data_2 = pd.Series([gauss(0.0, 1.0) for i in range(1000)])
    mysterious_data_2.name = 'White noise'
    mysterious_data_2.index = pd.date_range('1971-12-25 12:00', periods=1000, freq='3d')
    return mysterious_data_1, mysterious_data_2

def load_emissions_data():
    emissions = pd.read_csv('data/emissions.csv')
    emissions = emissions[emissions.Description=='Coal Electric Power Sector CO2 Emissions']
    emissions['YYYYMM'] = emissions['YYYYMM'].astype(str)
    emissions['YYYYMM'] = pd.to_datetime(emissions['YYYYMM'],format='%Y%m', errors='coerce')
    emissions = emissions.dropna()
    emissions = emissions.set_index('YYYYMM').sort_index()
    emissions.index = emissions.index.rename('date')
    emissions['Value'] = emissions.Value.astype(float)
    emissions = emissions['Value']
    emissions = emissions.loc['1980':'2000']
    emissions = emissions.asfreq('MS')
    return emissions # we want a series, not df

def load_coal_data():
    np.random.seed(10)
    df = pd.read_csv('data/MER_T06_01.csv')
    df = df[df.Description=='Coal Consumption']
    df.YYYYMM = pd.to_datetime(df.YYYYMM, format='%Y%m',errors='coerce' )
    df = df[['YYYYMM','Value']]
    df = df.dropna()
    df = df.set_index('YYYYMM').sort_index()
    df = df.loc["1980":"2000"]
    df.Value = pd.to_numeric(df.Value)
    df.Value = df.Value + np.random.normal(0,df.Value.mean()/20,len(df.Value))
    return df['Value'] # we want a series

def plot_conf_int_sarimax_forecast_results(original, results, results_label):
    plt.plot(original, label='original')
    plt.plot(results['mean'], label=results_label)
    plt.fill_between(results.index, results['mean_ci_upper'], 
                 results['mean_ci_lower'], color="tab:orange", alpha=0.15)
    plt.xlabel('Time')
    plt.title('# Passengers per month (in thousands)')
    plt.legend()

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
    