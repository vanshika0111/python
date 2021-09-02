# creating a python package using setuptools

"""
Steps:
    1. create a folder - Packages
    2. create a folder inside Package(step 1) - PackageOne
    3. inside Packages (step 1) - create two files: readme.txt & License.txt
    4. open vs code
    5. create one py file in Packages(step 1): setup.py 
    6. create one py file in PackageOne(step 2): __init__.py
    7. write the required in setup.py & __init__.py
    pip install wheel
    8. open terminal & run command: python setup.py stist bdist_wheel OR python setup.py bdist_wheel
    9. build & dist dir will be created
    10. cd dist
    11. pip install PackageOne
    12. on windwos powershell: python --> import PackageOne --> PackageOne.func(123)
"""

"""
__init__.py: - contains all the modules or def
setup.py: - all the access of modules or defs is written
"""