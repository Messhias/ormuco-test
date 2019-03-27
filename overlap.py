# Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and
# returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
# I will make the assumption that x1 is always smaller than x3
# I will make the assumption that x2 >= x1 and x4 >= x3
# Returns true if overlapping, False otherwise


def check_overlap(x1, x2, x3, x4):
    if x1 < x3 and x2 <= x3:
        return False
    elif x1 < x3 <= x2:
        return True
    elif x3 <= x1 and x4 <= x1:
        return False
    elif x3 <= x1 <= x4:
        return True

