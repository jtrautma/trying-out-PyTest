import pytest 

# Executes 3 "a-tests" x 2 "b-tests" = 3*2 = 6 tests.
# "DesignedToFail" will fail twice: once in combination w/ 'b1' and again in combination w/ 'b2'.
@pytest.mark.parametrize("a", ['a1', 'a2', 'designedToFail'])
@pytest.mark.parametrize("b", ['b1', 'b2'])
def test_nested_loop(a, b):
    assert a in ['a1', 'a2']
    assert b in ['b1', 'b2']