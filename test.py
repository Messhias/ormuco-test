from overlap import check_overlap


def overlap_test():
    """
        Test case for question A:

        Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the
        x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5)
        and (6,8).

        :return:
    """
    success = True

    if check_overlap(1, 2, 3, 4):
        success = False
        print('expected ' + str(False) +' but got ' + str((check_overlap(1, 2, 3, 4))))
    if not check_overlap(1, 3, 2, 4):
        success = False
        print('expected ' + str(True) + ' but got ' + str((check_overlap(1, 3, 2, 4))))
    if check_overlap(3, 4, 1, 2):
        success = False
        print('expected ' + str(False) +' but got ' + str((check_overlap(3, 4, 1, 2))))
    if not check_overlap(2, 4, 1, 3):
        success = False
        print('expected ' + str(True) + ' but got ' + str((check_overlap(2, 4, 1, 3))))
    if not check_overlap(2, 3, 1, 4):
        success = False
        print('expected ' + str(True) + ' but got ' + str((check_overlap(2, 3, 1, 4))))
    if not check_overlap(1, 4, 2, 3):
        success = False
        print('expected ' + str(True) + ' but got ' + str((check_overlap(1, 4, 2, 3))))
    if not check_overlap(1, 3, 1, 2):
        success = False
        print('expected ' + str(True) + ' but got ' + str((check_overlap(1, 3, 1, 2))))
    if not check_overlap(1, 4, 2, 4):
        success = False
        print('expected ' + str(True) + ' but got ' + str((check_overlap(1, 4, 2, 4))))

    if success:
        print('All overlapping tests successfully performed.\n')
    else:
        print('All overlapping tests performed. (With errors)\n')


print('Test for Question A: Overlapping lines')
overlap_test()

