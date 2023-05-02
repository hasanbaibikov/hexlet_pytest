def test_stack():
    stack = []
    stack.append('one')
    stack.append('two')


    assert stack.pop('two') == 'two'
    assert stack.pop('one') == 'one'


def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)


    stack.pop()
    assert not stack

