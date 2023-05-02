from example import reverse


def test_example():
    assert reverse('Hello') == 'olleH'


def test_example_for_empty_string():
    assert reverse('') == ''

