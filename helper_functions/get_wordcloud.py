import matplotlib.pyplot as plt
from wordcloud import WordCloud

def get_wordcloud(text, max_words, stop_words, filename):
    """
    Generate, display and return the wordcloud corresponding to the text provided as input.
    """
    # Generate a word cloud image.
    wordcloud = WordCloud(max_words=max_words, stopwords=stop_words, background_color='white').generate(text)

    # Display the generated image.
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    wordcloud.to_file(filename)
    plt.show()

    return wordcloud