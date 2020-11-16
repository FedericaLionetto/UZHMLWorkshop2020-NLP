def assign_label_recommended(df_row):
    """
    Return 0 if not recommended and 1 otherwise.
    """
    label_recommended = None
    if df_row['recommended'] == True:
        label_recommended = 1
    elif df_row['recommended'] == False:
        label_recommended = 0
    else:
        label_recommended = None
    return label_recommended