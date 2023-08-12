from hashlib import sha1

import json

try:
    import scraper as testfile

except ModuleNotFoundError:
    assert False, "The name of your file is supposed to be 'scraper.py'!"


def test_task2():

    result = testfile.scrape_books()

    assert type(result) is list, "Your function should return a list"
    assert len(result) > 0, "The list should not be empty!"
    assert type(result[0]) is dict, "Your function should return a list of dicts"
    assert "title" in result[0].keys(), "Your dicts need to have the key 'title'"
    assert "price" in result[0].keys(), "Your dicts need to have the key 'price'"

    expected = "dd630efe9877eca55337c91629d2887e41377082"

    filtered = [{"title": book["title"], "price": book["price"]} for book in result]

    jsonized = [json.dumps(d, sort_keys=True) for d in filtered]
    jsonized = json.dumps(jsonized)

    assert sha1(jsonized.encode("utf-8")).hexdigest() == expected, "Your function does not return the expected result!"
