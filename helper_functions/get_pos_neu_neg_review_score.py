def get_pos_neu_neg_review_score(df_row):
    """
    Return:
    - 'pos' if the review score is positive (>=7),
    - 'neu' if the review score is neutral (5 or 6),
    - 'neg' if the review score is negative (<=4).
    """
    pos_neu_neg_review_score = None
    if (df_row['review_score'] is None or str(df_row['review_score']) == '<NA>'):
        pos_neu_neg_review_score = None
    else:
        if (df_row['review_score'] <= 4):
            pos_neu_neg_review_score = 'neg'
        elif (df_row['review_score'] > 4 and df_row['review_score'] <= 6):
            pos_neu_neg_review_score = 'neu'
        else:
            pos_neu_neg_review_score = 'pos'
    return pos_neu_neg_review_score