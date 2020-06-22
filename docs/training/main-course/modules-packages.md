# We are the Mods: Modules & Package

## Basic Module and Package Layout
A typical Python code layout structures the code in package directories
and module files.

A very simple package structure could look like this:

```
mypackage/
mypackage/__init__.py
mypackage/module1.py
mypackage/module2.py
```

Suppose these files have the following contents:

``` python
--8<--
src/modules-packages/mypackage/__init__.py
--8<--
```

``` python
--8<--
src/modules-packages/mypackage/module1.py
--8<--
```

``` python
--8<--
src/modules-packages/mypackage/module2.py
--8<--
```

This package can now be used as follows:
``` python
>>> import mypackage
mypackage
>>> mypackage.module1.f()  # this will fail: mypackage.module1 not yet imported
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mypackage' has no attribute 'module1'
>>>
>>> import mypackage.module1
I'm module 1
>>> mypackage.module1.f()
Module 1 is great
>>> import mypackage.module2
I'm module 2
>>> mypackage.module2.f()
Module 2 is also great
>>>
>> import mypackage.module1 # 2nd import 
>>> 
```

Some things to note:

 - code in an `__init__.py`-file in a package dir gets executed when the
 package is imported
 - `__init__.py` code is just regular Python code
 - statements in a module get executed when the module is imported
 - modules are imported only once per interpreter session (you can enforce
 [reload in interactive sessions](https://docs.python.org/3/tutorial/modules.html#more-on-modules))

## Regular and Namespace Packages

## Module Search Path

Lookup of modules involves a search path. The search order for `mod.py` is

 1. look for a built-in module with that name
 1. look in the directories available in `sys.path` for the `mod.py` file

`sys.path` basically contains

 - the directory containing the importing file, or the current working
   directory if no file, i.e. in an interactive interpreter session
 - the directories set in the (optional) `PYTHONPATH` environment variable
 - the default directories of the Python installation, e.g. for a Python 3.6
   linux installation:

    ```
    .../lib/python3.6/                # stdlib
    .../lib/python3.6/lib-dynload/    # stdlib shared libraries
    .../lib/python3.6/site-packages/  # site-wide installed 3rd party packages
    ```


