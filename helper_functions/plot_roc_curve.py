import matplotlib.pyplot as plt
import seaborn as sns

def plot_roc_curve(fpr, tpr, clf_name, figsize_w, figsize_h, filename):
    """
    Plot the ROC curve of a classifier.
    """
    plt.figure(figsize=(figsize_w,figsize_h))
    sns.set(style="whitegrid")
    plt.plot([0, 1], [0, 1], 'k--', label='random')
    plt.plot(fpr, tpr, label=clf_name)
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.legend(loc='best')
    plt.savefig(filename)
    plt.show()
    return