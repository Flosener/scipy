import numpy as np

import types


def imports_of_your_file(filename, testfile):
    """ Yields all imports in the tested file. """

    for name, val in vars(testfile).items():
        if isinstance(val, types.ModuleType):
            # get direct imports
            yield val.__name__

        else:
            # get from x import y imports
            imprt = getattr(testfile, name)

            if hasattr(imprt, "__module__") and not str(imprt.__module__).startswith("_") and not str(imprt.__module__) == filename:
                yield imprt.__module__


def height(xy):
    """ Returns the height of the Mountains of Mordor at a given tuple (x, y) of coordinates. """

    return (-(xy[1] + 42) * np.sin(np.sqrt(abs(xy[0] / 2 + (xy[1] + 42)))) - xy[0] * np.sin(np.sqrt(abs(xy[0] - (xy[1] + 42)))))
