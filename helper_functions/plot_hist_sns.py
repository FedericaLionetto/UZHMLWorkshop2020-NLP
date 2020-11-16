import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist_sns(df,feat,bins,title,x_label,y_label,filename):
    """
    Plot the histogram of a given feature.
    """
    plt.figure(figsize=(6,6))
    sns.distplot(df[feat],bins=bins,kde=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(False)
    plt.savefig(filename)
    plt.show()
    return