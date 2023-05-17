import pytest

from richtypes import RichList, RichDict


@pytest.fixture
def rich_list() -> RichList:
    """
    This function is a Pytest fixture that returns a RichList object. The RichList object contains the numbers 1 through 11 inclusive. The function does not take in any parameters and returns a RichList object.

    :return: A RichList object containing the numbers 1 through 11 inclusive.
    :rtype: RichList
    """
    return RichList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)


@pytest.fixture
def rich_list_empty() -> RichList:
    """
    This function is a pytest fixture that returns an empty instance of the RichList class.

    Parameters:
    None

    Returns:
    A RichList object that is empty.
    """
    return RichList()


@pytest.fixture
def rich_dict() -> RichDict:
    """
    Generates a pytest fixture that returns a RichDict object with pre-defined keys and values.

    :return: A RichDict object with keys "one" through "eleven" and their corresponding values.
    :rtype: RichDict
    """
    return RichDict(
        one=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9,
        ten=10,
        eleven=11,
    )


@pytest.fixture
def rich_dict_empty() -> RichDict:
    """
    This function is a pytest fixture that returns an instance of the RichDict class.
    It does not take in any parameters and always returns an empty RichDict object.
    The return type of this function is RichDict.
    """
    return RichDict()
