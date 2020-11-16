import numpy as np
import matplotlib.pyplot as plt

def plot_word_cloud_diff(df_sorted, label_1, label_2, n_top_words, filename):
    """
    Given a Pandas data frame that contains the columns 'word' and 'diff' 
    and that is sorted by diff in decreasing order, 
    plot a bar chart corresponding to the first 'n_top_words' records.
    """
    fig, ax = plt.subplots(figsize=(8,10))
    df_plot = df_sorted[df_sorted['diff'].notna()]
    plot_words = df_plot['word'][:n_top_words]
    plot_values = df_plot['diff'][:n_top_words]
    y_pos = np.arange(plot_words.shape[0])
    ax.barh(y=y_pos,width=plot_values,align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(plot_words)
    ax.invert_yaxis()
    ax.set_xlabel(label_1+' - '+label_2)
    ax.set_title('Word cloud difference')
    plt.savefig(filename)
    plt.show()