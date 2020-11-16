def get_completeness(df_row):
    """
    Return true if the review contains all fields and false otherwise.
    """
    is_complete = None
    is_not_complete = df_row.isnull().any()
    if (is_not_complete == True):
        is_complete = False
    else:
        is_complete = True
    return is_complete