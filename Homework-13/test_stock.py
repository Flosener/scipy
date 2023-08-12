from hashlib import sha1

import json

try:
    import scraper as testfile

except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'scraper.py'!"


def test_task3():

    result = testfile.scrape_books()

    assert type(result) is list, "Your function should return a list"
    assert len(result) > 0, "The list should not be empty!"
    assert type(result[0]) is dict, "Your function should return a list of dicts"
    assert set(result[0].keys()) == {"title", "price", "stock"}, "The dicts do not contain the expected keys!"

    expected = "1cdbe7d03372864808fa6ca6d7e1fedb47996158"

    jsonized = [json.dumps(d, sort_keys=True) for d in result]
    jsonized = json.dumps(jsonized)

    assert sha1(jsonized.encode("utf-8")).hexdigest() == expected, "Your function does not return the expected result!"
