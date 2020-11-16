import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(df,feat,filename,horizontal=False,figsize_w=None,figsize_h=None):
    """
    Plot the bar of occurrences of each value of a given feature.
    """
    print('Feature: {}'.format(feat))
    keys_list = []
    entries_list = []
    keys = df[feat].unique()
    entries_dict = {}
    for key in keys:
        entries_dict[key] = np.sum(df[feat]==key)
    entries_dict_ordered = {k: v for k, v in sorted(entries_dict.items(), reverse=True, key=lambda item: item[1])}
    keys_list = list(entries_dict_ordered.keys())
    entries_list = list(entries_dict_ordered.values())
    print('Values of the feature:', keys_list)
    print('Frequencies of the feature:', entries_list)
    if figsize_w is not None and figsize_h is not None:
        plt.figure(figsize=(figsize_w,figsize_h))
    else:
        plt.figure(figsize=(6,6))
    sns.set(style="whitegrid")
    if horizontal==True:
        ax = sns.barplot(x=entries_list, y=keys_list,color="Red")
        ax.set(xlabel='Frequency', ylabel=feat)
    else:
        ax = sns.barplot(x=keys_list, y=entries_list,color="Red")
        ax.set(xlabel=feat, ylabel='Frequency')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    return