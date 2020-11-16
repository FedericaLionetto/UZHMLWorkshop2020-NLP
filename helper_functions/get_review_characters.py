def get_review_characters(df_row):
    """
    Return the number of characters in the review.
    """
    review_characters = None
    if (str(df_row['review_text'])=='nan' or df_row['review_text'] is None):
        review_characters = 0
    else:
        review_characters = len(df_row['review_text'])
    return review_characters