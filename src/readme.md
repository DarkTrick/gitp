# run
```
python3 gitp
```


# unit testing
```
python3 -m unittest
```

Remember that for `unittest`
- Files with tests must be named `test_*.py`
  - E.g. this does not work: `test.mypackage.py`
- Test functions must be named `test_*`


# Install & run (for testing):
Use the following commands to locally install and test your project
```
pip install .
# run project
gitp
```

*Note:* For reinstalling, first remove the `build` directory that was created. Otherwise the file structure will be messed up.

# Uninstall (for testing):
```
pip uninstall gitp
```

# Build Project (for distributing and system install):

```
pip install build # <-- only if not yet installed
python -m build
```

This will create a `./dist/[...].tar.gz` package. <br>
This file could not be ...
- ... [distributed on PyPI](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives)
- ... installed via `pip install ./dist/[...].tar.gz`

