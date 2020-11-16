def has_layover(df_row):
    """
    Return True if the review score corresponds to a flight with layover and False otherwise.
    """
    layover = False
    if df_row['layover'] is not None and str(df_row['layover']) != 'NA':
        layover = True
    return layover