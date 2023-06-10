# Function that prints integers;
def print_list_integer(my_list=[]):
    """Print int values in a list

    Args:
        my_list: a list of integers defaults to empty

    Returns:
        Nothing
    """
    for num in my_list:
        print("{}".format(num))
