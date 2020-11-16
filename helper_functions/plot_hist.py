import matplotlib.pyplot as plt

def plot_hist(df,feat,bins,filename,x_min=None,x_max=None):
    """
    Plot the histogram of occurrences of each value of a given feature.
    """
    print('Feature: {}'.format(feat))
    plt.figure(figsize=(6,6))
    plt.hist(df[feat],bins=bins,color='red')
    if x_min is not None and x_max is not None:
        plt.xlim(x_min,x_max)
    plt.xlabel(feat)
    plt.ylabel('Entries / bin')
    plt.savefig(filename)
    plt.show()
    return