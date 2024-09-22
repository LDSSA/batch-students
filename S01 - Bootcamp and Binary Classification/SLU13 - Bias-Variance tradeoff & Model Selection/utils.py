import numpy as np
import pandas as pd

from random import randint
import matplotlib.pyplot as plt

from mlxtend.plotting import plot_decision_regions

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression


def tv(a, b, c, x):
    return (a * (x ** 2)) + (b * x) + c


def fit_lin_reg(df):
    fig, ax = plt.subplots()
    df.plot(kind='scatter', x='age', y='minutes_per_day', ax=ax, alpha=.5);
    fit_line(df['age'], df['minutes_per_day'])
    plt.title('Linear regression fit')
    plt.legend()
    plt.show()


def fit_line(x, y):
    lr = LinearRegression()
    lr.fit(x.values.reshape(-1, 1), y)

    y_plot = lr.predict(x.values.reshape(-1, 1))

    plt.plot(x, y_plot, ls=':', c='r',
             label='prediction')


def fit_knn(x, y):
    model = KNeighborsRegressor(1)

    model.fit(x.values.reshape(-1, 1), y)

    y_plot = model.predict(x.values.reshape(-1, 1))
    plt.plot(x, y_plot, ls=':', c='r', label='prediction')


def fit_high_variance_algo(df):
    fig, ax = plt.subplots()
    df.plot(kind='scatter', x='age', y='minutes_per_day', ax=ax, alpha=.5);
    fit_knn(df['age'], df['minutes_per_day'])
    plt.title('High variance model fit')
    plt.legend()
    plt.show()


def generate_time_on_tv():
    space = [int(i) for i in np.linspace(10, 80, 100)]
    df = pd.DataFrame({'age': pd.Series(space)}).set_index('age', drop=False)

    a = 0.1467
    b = -14.67
    c = 382
    df['minutes_per_day_raw'] = df.index.map(lambda x: tv(a, b, c, x))

    np.random.seed(100)
    df['noise'] = [randint(0, 30) for i in range(len(df))]

    df['minutes_per_day'] = df['minutes_per_day_raw'] + df['noise']

    df.loc[35, 'minutes_per_day'] = 130
    df.loc[70, 'minutes_per_day'] = 50

    return df


def draw_points(X, y):
    plt.figure(figsize=(10, 10))
    plot_decision_regions(X.values, y.values, clf=lr, legend=2)
    plt.title("Logistic Regression (LR)")
    plt.show()


def plot_super_conservative(X, y):
    lr = LogisticRegression()
    lr.fit(X, y)
    preds = lr.predict(X)
    plt.figure(figsize=(10, 10))
    plot_decision_regions(X.values, y.values, clf=lr, legend=2)
    plt.title("Logistic Regression (LR)")
    plt.xlabel('Color')
    plt.ylabel('IBU')
    plt.show()
    return preds


def plot_super_flexible(X, y):
    knn_k1 = KNeighborsClassifier(n_neighbors=1)
    knn_k1.fit(X, y)
    preds = knn_k1.predict(X)
    plt.figure(figsize=(10, 10))
    plot_decision_regions(X.values, y.values, clf=knn_k1, legend=2)
    plt.title("KNN (k=1)")
    plt.xlabel('Color')
    plt.ylabel('IBU')
    plt.show()
    return preds


def plot_just_right(X, y):
    knn_k9 = KNeighborsClassifier(n_neighbors=9)
    knn_k9.fit(X, y)
    preds = knn_k9.predict(X)
    plt.figure(figsize=(10, 10))
    plot_decision_regions(X.values, y.values, clf=knn_k9, legend=2)
    plt.title("KNN (k=9)")
    plt.xlabel('Color')
    plt.ylabel('IBU')
    plt.show()
    return preds


def fit_and_plot_linear_regression(data):
    y = data['y']
    X = data.drop('y', axis=1)

    lr = LinearRegression(normalize=True)

    lr.fit(X, y)

    plt.scatter(X['x'], data['y'], c='orange', s=5)
    plt.plot(X['x'], lr.predict(X))
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression (R²: {})'.format(lr.score(X, y)))


def _get_min_max_mean(scores, train_sizes):
    return pd.DataFrame({'max': np.max(scores, axis=1),
                         'mean': np.mean(scores, axis=1),
                         'min': np.min(scores, axis=1)},
                        index=train_sizes)


def _plot_results(results, label):
    if label == 'train':
        color = 'blue'
    else:
        color = 'orange'

    ax = results['mean'].plot(label=label, marker='o')
    ax.fill_between(results.index,
                    results['min'],
                    results['max'],
                    facecolor=color,
                    alpha=0.1)


def plot_learning_curve(train_sizes_abs, train_scores, test_scores, y_label='roc_auc_score'):
    train_results = _get_min_max_mean(train_scores, train_sizes_abs)
    test_results = _get_min_max_mean(test_scores, train_sizes_abs)
    train_results = _get_min_max_mean(train_scores, train_sizes_abs)
    test_results = _get_min_max_mean(test_scores, train_sizes_abs)

    _plot_results(train_results, 'train')
    _plot_results(test_results, 'test')
            
    plt.legend()
    plt.xlabel('Number of training examples')
    plt.ylabel(y_label)
    plt.title('Learning curve')
    
    plt.show()

