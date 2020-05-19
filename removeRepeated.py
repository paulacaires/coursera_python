def remove_repetidos(numList):
    '''Receives: list of numbers
    Returns: New list without repeated numbers, but ordered.'''
    newList = list()
    for num in numList:
        if num not in newList:
            newList.append(num)
    return sorted(newList)

