from IPython import display
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import time

#color maps
rb_palette = sns.color_palette(palette = 'blend:blue,red', as_cmap = True)
blind_palette = sns.color_palette(palette = 'colorblind', as_cmap = True)
rb_11_palette = sns.color_palette(palette = 'blend:red,blue', n_colors = 11)

#need
def get_data_iris():
	X, Y = load_iris(return_X_y = True)
	X = pd.DataFrame(X, columns = ['SEPAL_LENGTH', 'SEPAL_WIDTH', 'PETAL_LENGTH', 'PETAL_WIDTH'])
	Y = pd.Series(Y, name = 'SPECIES')
	return X, Y

def flogistic(z):
    return 1/(1 + np.exp(-z))

def binary_univariate(X, y):
    y_binary = np.where(y == 0, 1, 0)
    X_binary = X[['PETAL_WIDTH']].to_numpy()
    #fit
    logit_binary = LogisticRegression(random_state = 42)
    logit_binary.fit(X_binary, y_binary)
    #plot
    data = pd.concat((X[['PETAL_WIDTH']], y),axis = 1)
    data['CLASSES'] = np.where(data.SPECIES == 0, 1, 0)
    g = sns.relplot(x= "PETAL_WIDTH", y = "CLASSES", data = data, hue = "CLASSES",
                    height = 3.5, markers = ".", palette = 'colorblind');
    petal_width = np.linspace(-1, 3)
    z = logit_binary.intercept_[0] + petal_width * logit_binary.coef_[0][0]
    data_clf = pd.DataFrame({'petal_width': petal_width, 'flogistic': flogistic(z)})
    sns.lineplot(x = 'petal_width', y = 'flogistic', data = data_clf, color = blind_palette[5], legend = None)
    g.set(xticks = [-1,-0.5,0,0.5,1,1.5,2,2.5]);
    g.set_axis_labels("PETAL_WIDTH", "estimated probability");
    g.legend.set_title("CLASSES");
    return logit_binary

def binary_univariate_boundary(X, y, logit_binary):
    data = pd.concat((X[['PETAL_WIDTH']], y), axis = 1)
    data['CLASSES'] = np.where(data.SPECIES == 0, 1, 0)
    g = sns.relplot(x = "PETAL_WIDTH", y = "CLASSES", data = data, hue = "CLASSES",
                    height = 3.5, markers = ".", palette = 'colorblind');
    petal_width = np.linspace(-1.2, 3)
    z = logit_binary.intercept_[0] + petal_width * logit_binary.coef_[0][0]
    data_clf = pd.DataFrame({'petal_width': petal_width, 'flogistic': flogistic(z)})
    sns.lineplot(x = 'petal_width', y = 'flogistic', data = data_clf, color = blind_palette[5], legend = None)
    g.set(xticks = [-1,-0.5,0,0.5,1,1.5,2,2.5]);
    boundary = -logit_binary.intercept_[0] / logit_binary.coef_[0][0]
    g.axes[0][0].axvline(x = boundary, color = blind_palette[2], linewidth = 1.5);
    g.set_axis_labels("PETAL_WIDTH", "estimated probability");
    g.legend.set_title("CLASSES");

def x_probability(p, clf):
    return (np.log(p / (1 - p)) - clf.intercept_[0]) / clf.coef_[0][0]
    
def binary_univariate_probability(logit_binary):
    petal_width = np.linspace(-1.5, 3)
    z = logit_binary.intercept_[0] + petal_width * logit_binary.coef_[0][0]
    data_clf = pd.DataFrame({'PETAL_WIDTH': petal_width, 'probability': flogistic(z)})
    g = sns.lineplot(x = 'PETAL_WIDTH', y = 'probability', data = data_clf, color = blind_palette[5])
    boundary = -logit_binary.intercept_[0] / logit_binary.coef_[0][0]
    prob = [0.95,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
    ymax = [0.91,0.86,0.76,0.67,0.57,0.475,0.39,0.31,0.22,0.13]
    for (i, p) in enumerate(prob):
        g.axes.axvline(x_probability(p, logit_binary), 0, ymax[i], 
                       color = rb_11_palette[i], linestyle = ':', linewidth = 1);
        g.axes.text(x_probability(p, logit_binary) + 0.1, p,
                    '{}%, {:.2f} cm'.format(p * 100, x_probability(p, logit_binary)),
                    size = 8, color = rb_11_palette[i]);
    g.axes.axvline(x_probability(.9999, logit_binary), 0, 0.96, color = rb_11_palette[0],
                   linestyle = ':', linewidth = 1);
    g.axes.text(x_probability(.9999, logit_binary) + 0.1, 0.93, '99.99%',
                size = 8, color = rb_11_palette[0]);
    g.axes.text(x_probability(.9999, logit_binary) + 0.1, 0.87, 
                '{:.2f} cm'.format(x_probability(.9999, logit_binary)), size = 8,
                color = rb_11_palette[0]);
    g.axes.axvline(x_probability(.0001, logit_binary), 0, 0.045,
                   color = rb_11_palette[10], linestyle = ':', linewidth = 1);
    g.axes.text(x_probability(.0001, logit_binary) - 0.5, 0.03, '0.0001%',
                size = 8, color = rb_11_palette[10]);
    g.axes.text(x_probability(.0001, logit_binary) - 0.9, -0.035,
                '{:.2f} cm'.format(x_probability(.0001, logit_binary)),
                size = 8, color = rb_11_palette[10]);

def binary_univariate_balanced(X, y):
    #balance classes
    y_balanced = np.where(y == 0, 1, 0)
    y_balanced = np.concatenate((y_balanced[0:50], y_balanced))
    X_balanced = pd.concat((X[['PETAL_WIDTH']].iloc[0:50], X[['PETAL_WIDTH']])).to_numpy()
    #fit balanced
    logit_balanced = LogisticRegression(random_state = 42)
    logit_balanced.fit(X_balanced, y_balanced)
    #fit imbalanced
    y_binary = np.where(y == 0, 1, 0)
    X_binary = X[['PETAL_WIDTH']].to_numpy()
    logit_binary = LogisticRegression(random_state = 42)
    logit_binary.fit(X_binary, y_binary)
    #plot
    data = pd.DataFrame({'PETAL_WIDTH': X_binary[:,0], 'CLASSES': y_binary})
    g = sns.relplot(x = "PETAL_WIDTH", y = "CLASSES", data = data, hue = "CLASSES",
                    height = 3.5, markers = ".", palette = 'colorblind');
    petal_width = np.linspace(-1, 3)
    z_balanced = logit_balanced.intercept_[0] + petal_width * logit_balanced.coef_[0][0]
    z = logit_binary.intercept_[0] + petal_width * logit_binary.coef_[0][0]
    data_binary = pd.DataFrame({'petal_width': petal_width,'flogistic': flogistic(z)})
    data_balanced = pd.DataFrame({'petal_width': petal_width, 'flogistic': flogistic(z_balanced)})
    sns.lineplot(x = 'petal_width', y = 'flogistic', data = data_binary, color = blind_palette[5], legend = None)
    sns.lineplot(x = 'petal_width', y = 'flogistic', data = data_balanced, color = blind_palette[9], legend = None)
    g.set(xticks = [-1,-0.5,0,0.5,1,1.5,2,2.5]);
    g.set_axis_labels("PETAL_WIDTH", "estimated probability");
    return logit_binary, logit_balanced

def odds_ratio(z):
    return flogistic(z) / (1 - flogistic(z))

def plot_odds_ratio():
    z = np.linspace(-10, 20)
    plt.plot(z, flogistic(z), label = 'probability');
    plt.plot(z, odds_ratio(z), label = 'odds ratio');
    plt.plot([0, 0], (-1, 1), linestyle = ':', linewidth = 1, label = 'decision boundary')
    plt.ylim(-1, 5);
    plt.xlabel('z');
    plt.ylabel('OR / p');
    plt.legend(loc = 'lower right', fontsize = 'small');

def multivariate_3d_plot(X, y):
    data = pd.concat((X, y), axis = 1)
    data = data.loc[data.SPECIES != 0]
    data['CLASSES'] = np.where(data.SPECIES == 2, 1, 0)
    g = plt.figure().add_subplot(projection = '3d');
    g.scatter(data['PETAL_WIDTH'], data['SEPAL_WIDTH'], data['CLASSES'], marker = 'o',
              c = data['CLASSES'].map(lambda x: blind_palette[x]));
    g.set_xlabel('PETAL_WIDTH');
    g.set_ylabel('SEPAL_WIDTH');
    g.set_zlabel('CLASS');
    g.zaxis.set_ticks([0, 1])
    plt.show();

def multivariate_boundary_2d(X, y, logit_multivariate):
    pw, sw = np.mgrid[0.75:2.75:.01,1.75:4:.01]
    grid = np.c_[pw.ravel(), sw.ravel()]
    surf = logit_multivariate.predict_proba(grid)[:, 1].reshape(pw.shape)

    petal_width = np.linspace(1, 2.5)
    sepal_width = (-logit_multivariate.intercept_[0] / logit_multivariate.coef_[0][1]-
              logit_multivariate.coef_[0][0] / logit_multivariate.coef_[0][1] * petal_width)
    boundary = pd.DataFrame({'petal_width': petal_width,'sepal_width': sepal_width})
    data = pd.concat((X, y), axis = 1)
    data = data.loc[data.SPECIES != 0]
    data['CLASSES'] = np.where(data.SPECIES == 2, 1, 0)
    g = sns.relplot(x = "PETAL_WIDTH", y = "SEPAL_WIDTH", data = data, hue = "CLASSES", height = 3);
    plt.contourf(pw, sw, surf, 25, cmap = rb_palette, vmin = 0, vmax = 1, zorder = -1);
    sns.lineplot(x = 'petal_width', y = 'sepal_width', data = boundary, color = 'white', legend = None);
    g.ax.set(ylim = (1.75, 4));

def flogistic_2d(x, y, b0, b1, b2):
    z = b0 + x * b1 + y * b2
    return 1 / (1 + np.exp(-z))
    
def multivariate_boundary_3d(X, y, logit_multivariate):
    pw, sw = np.mgrid[0.75:2.75:.01,1.75:4:.01]
    f_2d = flogistic_2d(pw, sw, logit_multivariate.intercept_[0], logit_multivariate.coef_[0][0],
       logit_multivariate.coef_[0][1])    

    sepal_width = np.linspace(1.75, 3.75)
    petal_width = (-logit_multivariate.intercept_[0] / logit_multivariate.coef_[0][0]-
              logit_multivariate.coef_[0][1] / logit_multivariate.coef_[0][0] * sepal_width)
    line_z = np.ones(petal_width.shape[0]) * 0.5

    data = pd.concat((X, y), axis = 1)
    data = data.loc[data.SPECIES != 0]
    data['CLASSES'] = np.where(data.SPECIES == 2, 1, 0)

    g = plt.figure(figsize = (5, 5)).add_subplot(projection = '3d');
    g.scatter(data['PETAL_WIDTH'], data['SEPAL_WIDTH'], data['CLASSES'], marker = 'o',
              c = data['CLASSES'].map(lambda x: blind_palette[x]));
    g.plot_surface(pw, sw, f_2d, cmap = rb_palette)
    g.plot3D(petal_width, sepal_width, line_z, 'black')
    g.set_xlabel('PETAL_WIDTH', labelpad = 9);
    g.set_ylabel('SEPAL_WIDTH');
    g.set_zlabel('probability');
    g.axes.tick_params('x', labelsize = 9, pad = 0.1, labelrotation = 60)
    g.view_init(30, -75) #default 30,-60
    plt.show();

def gradient_descent_classification_plot(X, Y, iter):
    probs = []
    coefs = []
    icepts = []
    data = pd.concat((X, Y), axis = 1)
    xx, yy = np.mgrid[4:8:.01, 0:2.8:.01] #grid for coordinates of surface
    grid = np.c_[xx.ravel(), yy.ravel()] #grid for probabilities surface to plot contour
    species = 2
    x_data=data.loc[data.SPECIES != species,['SEPAL_LENGTH', 'PETAL_WIDTH']]
    y_data=data.loc[data.SPECIES != species, 'SPECIES']
    labels = y_data.unique()
    clf = LogisticRegression(max_iter=1, warm_start = True, solver = 'sag', random_state=0).fit(x_data, y_data)
    for i in range(iter):
        clf.fit(x_data, y_data)
        probs.append(clf.predict_proba(grid)[:, 1].reshape(xx.shape))
        coefs.append(clf.coef_)
        icepts.append(clf.intercept_)
    f, ax = plt.subplots(figsize=(8, 6));
    for i in range(iter):
        display.clear_output(wait = True);
        time.sleep(0.5)
        contour = ax.contourf(xx, yy, probs[i], 25, cmap = rb_palette, vmin = 0, vmax = 1)
        ax.scatter(x = x_data['SEPAL_LENGTH'], y = x_data['PETAL_WIDTH'], c = y_data,
		       s = 50, cmap = rb_palette, vmin = -.2, vmax = 1.2, edgecolor = "white", linewidth = 1);
        ax.set(aspect = "equal",
		       xlim = (4, 8), ylim=(0, 2.8),
		       xlabel = "SEPAL_LENGTH", ylabel = "PETAL_WIDTH", 
               title = "Logistic Regression Classification Between Species %0.1i and %0.1i \n iteration %0.1i \n" % (labels[0],
                        labels[1], i + 1) + r"$\beta_0$ = %f $\beta_1$ = %f $\beta_2$ = %f" % (icepts[i][0],
                        coefs[i][0,0], coefs[i][0,1]));
        if (i == 0):
            ax_c = f.colorbar(contour);
            ax_c.set_label("P (Species = %0.1i)"%labels[1]);
            ax_c.set_ticks([0, .25, .5, .75, 1]);
        display.display(plt.gcf());
    plt.clf();


def plot_log_likelihood():
    x = np.linspace(1e-15, 1-1e-15, 1000)
    f, axs = plt.subplots(1, 2, figsize = (8, 3.5))
    plt.subplots_adjust(wspace = 0.3)
    ax = axs[0]
    ax.set(xlabel = r"$\hat{p}$", ylabel = "log-likelihood", title = "Log-likelihood for y = 0")
    ax.plot(x, np.log(1 - x))
    ax = axs[1]
    ax.set(xlabel = r"$\hat{p}$", ylabel = "log-likelihood", title = "Log-likelihood for y = 1")
    ax.plot(x, np.log(x))

def compare_classifiers(clf1, clf2, data1, data2, y):
    data1_standard = StandardScaler().fit_transform(data1)
    p1 = clf1.predict(data1_standard)
    data2_standard = StandardScaler().fit_transform(data2)
    p2 = clf2.predict(data2_standard)
    return (y == p1).sum(), (y == p2).sum()

def plot_exercise_boundary(dataset, features, y):
    X = dataset[features]
    X_standard = StandardScaler().fit_transform(X)

    clf = LogisticRegression(max_iter = 100, random_state = 100)
    clf.fit(X_standard, y)
    coef = clf.coef_
    intercept = clf.intercept_[0]

    plt.scatter(X_standard[:,0], X_standard[:,1], c = y, marker = '.');
    plt.xlabel(features[0]);
    plt.ylabel(features[1])
    xx = np.linspace(min(X_standard[:, 0]), max(X_standard[:, 0]))
    boundary = -(intercept + coef[0][0] * xx) / coef[0][1]
    plt.plot(xx, boundary);
    