import pandas as pd

def get_df_word_importance(dict_1, dict_2, label_1, label_2):
    """
    Create a Pandas data frame that contains the words appearing in two different word clouds
    and the importance of each word in each word cloud, 
    as well as the difference between the two. 
    """
    words_wordcloud = list(set(list(dict_1.keys())+list(dict_2.keys())))
    print('Total number of words in the two word clouds to compare: {:d}'.format(len(words_wordcloud)))

    df_1 = pd.DataFrame(dict_1.items(),columns=['word',label_1])
    df_2 = pd.DataFrame(dict_2.items(),columns=['word',label_2])
    df_1.set_index('word',inplace=True)
    df_2.set_index('word',inplace=True)

    df_wordcloud = pd.concat([df_1,df_2],axis=1,join='outer')

    df_wordcloud['diff'] = df_wordcloud[label_1]-df_wordcloud[label_2]
    df_wordcloud.sort_values(by='diff',ascending=False,inplace=True,axis=0)
    df_wordcloud.reset_index(inplace=True)
    df_wordcloud.rename(columns={'index':'word'},inplace=True)

    print(df_wordcloud.head())
    return df_wordcloud