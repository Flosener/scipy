from helpers import imports_of_your_file

import hashlib

try:

    import dijkstra as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'dijkstra.py'!"


def test_find_shortest_path(filename="dijkstra", allowed_imports={"scipy", "scipy.sparse", "scipy.spatial", "numpy"}):
    """ Checks whether find_shortest_path returns the correct shortest path."""

    assert testfile.find_shortest_path("The Shire", "Mount Doom") == ["The Shire", "Isengard", "Minas Morgul", "Mount Doom"]
    assert testfile.find_shortest_path("Rivendell", "Mount Doom") == ["Rivendell", "Misty Mountains", "Minas Morgul", "Mount Doom"]
    assert testfile.find_shortest_path("Isengard", "Helm's Deep") == ["Isengard", "Helm's Deep"]

    path = testfile.find_shortest_path("Rivendell", "Minas Morgul")
    assert hashlib.sha256(str(path).encode("utf-8")).hexdigest() == "d8895c30f828baae247ae19dc5bbe879249ba92172a7ece34b8d2dcfffb808b1"

    assert set(imports_of_your_file(filename, testfile)) <= allowed_imports, "You are not allowed to import any modules except NumPy and SciPy!"
