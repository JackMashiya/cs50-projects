from twttr import shorten


def test_lowercase():
    if shorten("hello") != "hll":
        raise Exception("Expected 'hll' for 'hello'")
    if shorten("twitter") != "twttr":
        raise Exception("Expected 'twttr' for 'twitter'")


def test_uppercase():
    if shorten("HELLO") != "HLL":
        raise Exception("Expected 'HLL' for 'HELLO'")
    if shorten("TWITTER") != "TWTTR":
        raise Exception("Expected 'TWTTR' for 'TWITTER'")


def test_mixed_case():
    if shorten("CS50") != "CS50":
        raise Exception("Expected 'CS50' for 'CS50'")
    if shorten("Python") != "Pythn":
        raise Exception("Expected 'Pythn' for 'Python'")


def test_numbers():
    if shorten("12345") != "12345":
        raise Exception("Expected '12345' for '12345'")


def test_punctuation():
    if shorten("hello!") != "hll!":
        raise Exception("Expected 'hll!' for 'hello!'")
    if shorten("what’s up?") != "wht’s p?":
        raise Exception("Expected 'wht’s p?' for 'what’s up?'")
