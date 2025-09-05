from fuel import convert, gauge

def test_convert_valid():
    if convert("1/2") != 50:
        raise Exception("Expected 50 for '1/2'")
    if convert("3/4") != 75:
        raise Exception("Expected 75 for '3/4'")
    if convert("1/100") != 1:
        raise Exception("Expected 1 for '1/100'")
    if convert("99/100") != 99:
        raise Exception("Expected 99 for '99/100'")


def test_convert_errors():
    try:
        convert("3/2")
        raise Exception("Expected ValueError for '3/2'")
    except ValueError:
        pass

    try:
        convert("1/0")
        raise Exception("Expected ZeroDivisionError for '1/0'")
    except ZeroDivisionError:
        pass

    try:
        convert("cat/dog")
        raise Exception("Expected ValueError for 'cat/dog'")
    except ValueError:
        pass

def test_gauge_empty_full():
    if gauge(0) != "E":
        raise Exception("Expected 'E' for 0%")
    if gauge(1) != "E":
        raise Exception("Expected 'E' for 1%")
    if gauge(99) != "F":
        raise Exception("Expected 'F' for 99%")
    if gauge(100) != "F":
        raise Exception("Expected 'F' for 100%")

