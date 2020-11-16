import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y, y_pred, normalize_str, figsize_w, figsize_h, filename):
    """
    Plot the confusion matrix of a classifier.
    """
    plt.figure(figsize=(figsize_w,figsize_h))
    plt.title('Confusion matrix')
    cm = confusion_matrix(y, y_pred, normalize=normalize_str)
    df_cm = pd.DataFrame(cm, columns=np.unique(y), index = np.unique(y))
    df_cm.index.name = 'Actual'
    df_cm.columns.name = 'Predicted'
    sns.set(font_scale=1.4) # For label size.
    sns.heatmap(df_cm, cmap="Reds", annot=True,annot_kws={"size": 16}) # For font size.
    plt.savefig(filename)
    plt.show()
    return