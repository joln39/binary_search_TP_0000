from main  import binary_search

def test_binary_search_1():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    result = binary_search(arr, target)
    assert result == 3
def test_binary_search_0():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = -6
    result = binary_search(arr, target)
    assert result == -1