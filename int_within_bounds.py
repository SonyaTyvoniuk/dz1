def int_within_bounds(number, lower_bound, upper_bound):
    if type(number) != int:
        return False
    elif number >= lower_bound and number < upper_bound:
        return True
    else:
        return False
    print(int_within_bounds(3, 1, 9))
    print(int_within_bounds(6, 1, 6))
    print(int_within_bounds(4.5, 3, 8))