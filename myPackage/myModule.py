def top_n(items, n):
    """Return the top n items in an array
        in descending order.

    Args:
        items(array): list or array like object.
        n(int): number of items to return.

    Return:
        array: top n items, in desc order.

    Egs:
        >>> top_n([8,3,2,74], 3)
        [8,7,3]
    """
    for i in range(n):  # Sorting is done until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+i]:  # if this item is bigger than the next item
                items[j], items[j+i] = items[j+i], items[j]  # Swap the two

    # Get the last two items
    top_n = items[-n:]

    # Return in descending order
    return top_n[::-1]
