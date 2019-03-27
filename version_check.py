# The goal of this question is to write a software library that accepts 2 version string as input and returns whether
# one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all
# test cases you could think of. I will make the assumption that versions are of format major.minor.release.build
# returns 1 if v1 is newer than v2, returns 0 if same version returns -1 if v1 is older than v2


def check_version(v1, v2):
    """
        Function to check the version of something.

        :param v1:
        :param v2:
        :return:
    """
    x1 = v1.split('.')
    x2 = v2.split('.')

    if len(x1) < max(len(x1), len(x2)):
        x1 = x1 + [0] * (len(x2) - len(x1))
    elif len(x2) < max(len(x1), len(x2)):
        x2 = x2 + [0] * (len(x2) - len(x1))

    for i in range(0, len(x1)):
        if int(x1[i]) > int(x2[i]):
            return 1
        elif int(x1[i]) < int(x2[i]):
            return -1

    return 0
