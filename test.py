from overlap import check_overlap
from version_check import check_version


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


def version_test():
    """
        Test case for question B:

        The goal of this question is to write a software library that accepts 2 version string as input and
        returns whether one is greater than, equal, or less than the other. As an example: “1.2” is
        greater than “1.1”. Please provide all test cases you could think of.

        :return:
    """
    success = True

    if check_version('1', '2') != -1:
        success = False
        print(check_version('1', '2'))
    if check_version('1.1', '1.2') != -1:
        success = False
        print(check_version('1.1', '1.2'))
    if check_version('1.3', '1.3.1') != -1:
        success = False
        print(check_version('1.3', '1.3.1'))
    if check_version('1.4', '1.3.12') != 1:
        success = False
        print(check_version('1.4', '1.3.12'))
    if check_version('3.1.1', '3.1.10') != -1:
        success = False
        print(check_version('3.1.1', '3.1.10'))
    if check_version('3.1.1.4321', '3.1.1.4321') != 0:
        success = False
        print(check_version('3.1.1.4321', '3.1.1.4321'))
    if check_version('2', '1') != 1:
        success = False
        print(check_version('2', '1'))
    if check_version('4.2', '1.2') != 1:
        success = False
        print(check_version('4.2', '1.2'))
    if check_version('1.1', '2') != -1:
        success = False
        print(check_version('1.1', '2'))
    if check_version('3.1.3', '3.1.3') != 0:
        success = False
        print(check_version('3.1.3', '3.1.3'))
    if check_version('1', '1.1.12.4444') != -1:
        success = False
        print(check_version('1', '1.1.12.4444'))

    if success:
        print('All version tests successfully performed.\n')
    else:
        print('All version tests performed. (With errors)\n')


print('Test for Question A: Overlapping lines')
overlap_test()


print('Test for Question B: Version check')
version_test()