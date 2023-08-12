from hashlib import sha1

try:
    import quiz as testfile

except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'quiz.py'!"


def test_task1():

    assert type(testfile.PRODUCT_CARD_CLASS_NAME) is str
    assert type(testfile.TITLE_ATTRIBUTE_NAME) is str
    assert type(testfile.PRICE_CLASS_NAME) is str
    assert type(testfile.STOCK_TAG_NAME) is str
    assert type(testfile.ROW_NUMBER) is int

    expected = "593c60473da56ef792e5ce47faa8792ab6fa3b58"
    assert sha1(testfile.PRODUCT_CARD_CLASS_NAME.encode("utf-8")).hexdigest() == expected, "PRODUCT_CARD_CLASS_NAME incorrect"
    
    expected1 = "325562c769da3f80d0e63bb56514bc2e2723c9b5"
    expected2 = "3c6de1b7dd91465d437ef415f94f36afc1fbc8a8"
    actual = sha1(testfile.TITLE_ATTRIBUTE_NAME.encode("utf-8")).hexdigest()

    assert actual == expected1 or actual == expected2, "TITLE_ATTRIBUTE_NAME incorrect"

    assert sha1(testfile.PRICE_CLASS_NAME.encode("utf-8")).hexdigest() == "56d8fa5e1e87c9c943ee180abda983d7f6fbd3b8", "PRICE_CLASS_NAME incorrect"
    assert sha1(testfile.STOCK_TAG_NAME.encode("utf-8")).hexdigest() == "c156a3b8932142e3458414ef88c2d9c42a451b1b", "STOCK_TAG_NAME incorrect"
    assert sha1(repr(testfile.ROW_NUMBER).encode("utf-8")).hexdigest() == "ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4", "ROW_NUMBER incorrect"
