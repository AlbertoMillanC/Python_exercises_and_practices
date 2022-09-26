#"//how to use this library  for testing purposes only"?
PYTHONPATH=path/to/fooproject:$PYTHONPATH python foo/quux/corge.py


import sys
import os


if __name__ == "__main__":
    # I'm two levels deep in the package so package directory is
    packagedir = os.path.abspath(os.path.join(os.path.dirname(__file__),
        "..", ".."))
    sys.path.insert(0, packagedir)
    


