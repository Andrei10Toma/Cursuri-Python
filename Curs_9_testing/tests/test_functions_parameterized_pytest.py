import pytest
from functions import iter_sum, MyIterator


@pytest.mark.parametrize('iterator', (
        [1, 2, 3],
        (1, 2, 3),
        MyIterator()
))
def test_iter_sum(iterator):
    result = iter_sum(iterator)
    expected_result = 6

    assert result == expected_result


@pytest.mark.parametrize('non_iterator', (
    'abc',
    27,
    None,
    True,
    ))
def test_iter_sum_with_exception(non_iterator):
    with pytest.raises(TypeError) as type_error:
        iter_sum(non_iterator)

    print(type_error.value)
