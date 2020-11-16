import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_importance(features_names, features_importances, figsize_w, figsize_h, filename):
    """
    Plot the feature importance of a model.
    """
    plt.figure(figsize=(figsize_w,figsize_h))
    sns.set(style="whitegrid")
    plt.title("Feature importance")
    plt.bar(range(len(features_names)), features_importances, color="r", align="center")
    plt.xticks(range(len(features_names)),features_names, rotation='vertical')
    # plt.yticks(range(50), indices[50])
    plt.xlim([-1, len(features_names)])
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    return