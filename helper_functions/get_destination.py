def get_destination(df_row):
    """
    Return the destination of the flight.
    """
    destination = None
    if str(df_row['route'])=='nan':
        destination = None
    else:
        # print(df_row['route'])
        temp = df_row['route'].split(' to ')
        # Standard case, there is a string before ' to ' and a string after ' to '.
        if len(temp)==2:
            destination = temp[1].split(' via ')[0]
        # Special case, the second space in ' to ' is missing.
        elif len(temp)==1:
            temp2 = df_row['route'].split(' to')
            if len(temp2)==2:
                destination = temp2[1].split(' via ')[0]
        else:
            destination = None
    return destination