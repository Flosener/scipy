import types

def imports_of_your_file(filename, testfile):
    """ Yields all imports in the testfile. """

    for name, val in vars(testfile).items():
        if isinstance(val, types.ModuleType):
            # get direct imports
            yield val.__name__

        else:
            # get from x import y imports
            imprt = getattr(testfile, name)

            if hasattr(imprt, "__module__") and not str(imprt.__module__).startswith("_") and not str(imprt.__module__) == filename:
                yield imprt.__module__

