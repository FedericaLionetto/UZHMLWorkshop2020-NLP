def get_review_words(df_row):
    """
    Return the number of words in the review.
    """
    review_words = None
    if (str(df_row['review_text'])=='nan' or df_row['review_text'] is None):
        review_words = 0
    else:
        review_words = len(df_row['review_text'].split(' '))
    return review_words