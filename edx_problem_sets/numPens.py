def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if n == 0:
        return True
    
    elif n < 0:
        return False

    elif numPens(n - 24) or numPens(n - 8) or numPens(n - 5):
        return True

    else:
        return False
