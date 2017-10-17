import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Dimensionality")


def get_dim(obj):
    """
    This function runs in O(mn) time where
    m = the dimensionality of the array
    n = the number of elements in the longest list

    At the minimum you have to recurse on every list element so this
    efficiency cannot be improved
    """

    max_dim = 1
    for elt in obj:

        if isinstance(elt, list):
            max_dim = max(max_dim, get_dim(elt) + 1)

    return max_dim


def main():
    logger.info("Running test suite...")

    test_cases = [
        ([], 1),
        ([2], 1),
        ([[1]], 2),
        ([1, [[2, 3]]], 3),
        ([[2], [2, [3]]], 3),
        ([[[[[1], 2, 3, 4]]]], 5)
    ]

    for test in test_cases:
        logger.info("get_dim({}) == {}".format(test[0], test[1]))

        try:
            assert get_dim(test[0]) == test[1]
        except AssertionError:
            logger.error("Test case {} failed!".format(test))
            return

    logger.info("All tests passed!")


if __name__ == "__main__":
    main()
