# Python environments and (3rd party) package installation

## The Python's Nest

A typical system Python installation (on a Linux system) will look something 
like this:

```
/usr/bin/python -> python3.6
/usr/bin/python3 -> python3.6
/usr/bin/python3.6
/usr/include/python3.6 -> python3.6m
/usr/include/python3.6m
/usr/lib/python3.6
```

The `lib` path contains the Python standard library, basically:

```
/usr/lib/python3.6              # pure-python stdlib modules/packages
/usr/lib/python3.6/lib-dynload  # shared libraries (compiled C extensions)
```

But there's also the `site-packages` directory for system-wide installation of
3rd party libraries (i.e. not bundled with Pytho in its stdlib):
```
/usr/lib/python3.6/site-packages  # path for additional, non-standard packages
```

To install anything into these paths you usually need admin privileges (on
Linux, these paths are normally owned by the `root` user).

The benefit of installing additional packages to the system-wide installation
is obvious: all Python programs can then use these added functionality, and the
necessary library files are installed only once.

Most of the time, it is however less desirable to install your dependencies
(the 3rd party packages your program depends on) to the system Python
installation:

 - you might not even have admin privileges so you can't properly install your
   dependencies (the usual cas in corporate environments)
 - another program might require the same dependency albeit in a different,
   potentially conflicting version
 - it is harder to create portable programs as the next machine might *not*
   have the same packages installed, so your program won't run there

## Installing Python Packages
Python packages can be installed using the Python package installer
[`pip`](https://pip.pypa.io/en/stable/).

Usually such packages are retrieved from the official
[Python Package Index (PyPI)](https://pypi.org/).

!!! warning
    To avoid unintentional installation of malicious packages **always** make
    sure you 
    
     - know exactly what your installing (ideally having reviewed the code) and
     - use the **correct spelling** of the package you intend to install.

    There have been
    [attempts in the past](https://www.zdnet.com/article/two-malicious-python-libraries-removed-from-pypi/)
    to put malicious code on PyPI; these used the
    [typosquatting technique](https://en.wikipedia.org/wiki/Typosquatting) and 
    mimicked popular libraries by using a similar package name.[^securing-pypi]

    Unfortunately this is often not that easy because your dependency will
    probably depend on other packages itself (and so on), so the dependency
    tree can quickly become quite large...

[^securing-pypi]:
    There are
    [ongoing efforts to improve PyPI security](https://www.python.org/dev/peps/pep-0458/)
    and guard against evil-doers.

Using the popular [`requests` library]() as an example:

Install the latest & greatest version:
```
pip install "requests"
```

You can explicitly select a specific version for installation:

```
pip install "requests==2.23.0"
```

It's also possible to select a version inside some version range:

```
pip install "requests>=1,<2"
```

`pip` also allows you to select a version that is deemed compatible to 
another version (according to certain criteria of
compatibility):[^package-version-spec]

[^package-version-spec]: See https://www.python.org/dev/peps/pep-0440/.

```
pip install "requests~=2.19.0"
```

If the package to install is properly set up, `pip` resolves *its* dependencies
and automatically installs these "prerequisites", i.e. the dependencies of your
dependencies.

See here for more detailed
[tutorial instructions on installing packages](https://packaging.python.org/tutorials/installing-packages/).


## Python environments

If you don't want to install to the system Python (which is probably a good
idea) you can isolate your app and its dependencies in a Python "virtual
environment" or "venv". Virtual environments are installation directories that
basically contain a Python installation layout that "links" to the system
installation. In effect all the system Python installation stuff
(standard library etc.) is retrieved from this installation while your app and
its dependencies are installed into the `site-packages` directory of the
virtual environment.

A virtual env can simply be created with 

```
python3 -m venv /path/to/new/virtual-env
```

To use the virtual environment you can either
 - explitly use the executable path(s) of this virtual env:

     ```
     /path/to/new/virtual-env/bin/python  # interpreter
     /path/to/new/virtual-env/bin/pip     # package installer
     ```
 - or you can *activate* this environment:

     ```
     # POSIX (Linus e.a.)
     source /path/to/new/virtual-env/bin/activate           # bash/zsh
     source /path/to/new/virtual-env/bin/activate.csh       # csh/tcsh
     
     # Windows 
     C:\> \path\to\new\virtual-env\Scripts\activate.bat     # cmd.exe
     PS C:\> \path\to\new\virtual-env\Scripts\Activate.ps1  # PowerShell
     ```

Activation means "sourcing" a script that makes the necessary environment
settings (e.g. the program search path (`PATH` on Linux)) so that this virtual
env can be used without qualified path invocation. Once activated you can
simply use `python3`, `pip`, ... and the executable files in
`/path/to/new/virtual-env/bin/` are invoked. That means installing
packages with `pip` will now install these to the active virtual env.

To remind you you're working within an activated virtual env, activation
conveniently modifiies the command line prompt. 

Finally, you can leave activation using `deactivate`:

```
0 lisa@devmachine .../~ $ source ~/venvs/six-venv/bin/activate
(six-venv) 0 lisa@devmachine .../~ $
(six-venv) 0 lisa@devmachine .../cpycourse $ deactivate
0 lisa@devmachine .../~ $ 
```
