# Excursion: Shells

No program runs without context. In application programming this would usually
be a "shell" - a special program that provides operating system services and
environment to the user or other programs.



## Shell Cheat Sheet

| Subject                                         | Linux Bash command 1)         | Windows Powershell command 1)   | Notes     |
| ----------------------------------------------- | ----------------------------- | ----------------------------    | --------- |
| **Shell**                                       |                               |                                 |           |
| shell version                                   | bash --version                | $PSVersionTable                 |           |
| list available commands                         | compgen -c \| sort \| uniq    | get-command                     | 2)        |
| command help                                    | \<command\> --help            | help \<command\                 |           |
| shell command history                           | history                       | history                         |           |
| search shell command history                    | \<ctrl\>-r                    | \<ctrl\>-r                      |           |
| shell command navigation                        | \<arrow-up\> or \<arrow-down\>| \<arrow-up\> or \<arrow-down\>  |           |
| **Directories**                                 |                               |                                 |           |
| show current working directory                  | pwd                           | pwd                             |           |
| change drive                                    | NOT-AVAILABLE                 | C:                              |           |
| list directory content                          | ls                            | ls                              |           |
| list directory content using wildcards          | ls foo*                       | ls foo*                         |           |
| list directory tree                             | tree -L \<level\>             | tree                            |           |
| change directory                                | cd \<directory\>              | cd \<directory\>                |           |
| create directory                                | mkdir FOO                     | mkdir FOO                       |           |
| remove/delete directory                         | rmdir FOO                     | rmdir FOO                       |           |
| move (and/or rename) directory                  | mv FOO BAR                    | mv FOO BAR                      |           |
| **Files**                                       |                               |                                 |           |
| create file                                     | touch foo.txt                 | new-item foo.txt -itemtype file |           |
| copy file                                       | cp foo.txt bar.txt            | cp foo.txt bar.txt              |           |
| remove/delete file                              | rm bar.txt                    | rm bar.txt                      |           |
| move (and/or rename) file                       | mv foo.txt bar.txt            | mv foo.txt bar.txt              |           |
| append content to a text-file ('>>'-operator)   | echo "Hello World" >> bar.txt | echo "Hello World" >> bar.txt   |           |
| overwrite content of a text-file ('>'-operator) | echo "Hello World" > bar.txt  | echo "Hello World" > bar.txt    |           |
| show text-file content                          | cat bar.txt                   | cat bar.txt                     |           |
| **Environment Variables**                       |                               |                                 |           |
| list all environment variables                  | env                           | ls env:                         |           |
| some predefined environment variables           | USER, HOME, PATH              | USERNAME, HOMEPATH, PATH        |           |
| get/show environment variable                   | echo $\<variable\>            | $env:\<variable\>               |           |
| set environment variable                        | FOO=foo                       | $env:FOO="foo"                  | 3)        |
| extend value of environment variable            | FOO+=$USER                    | $env:FOO += $env:USERNAME       |           |
| remove/delete environment variable              | unset FOO                     | remove-item env:FOO             |           |
| **Shell script example**                        |                               |                                 |           |
| Using environment variable and calling Python   | see test-env.sh in 4)         | see test-env.ps1 5)             |           |



**Footnotes**
1) Case-Sensitivity: Bash is case-sensitive, as opposed to Powershell, which is case-insensitive
2) Bash: There is no single command to list all avaliable Unix commands. Instead the 'compgen'-command list all available Bash builtins, command-aliases and executables found in the PATH variable
3) Variable-Assignment: In Bash no 'blanks' allowed between variable-name, assignment-operator ('=') and value; Powershell instead allows 'blanks', but needs apostroph, if the value is a string
4) Bash-script using environment variable and calling Python
    # test-env.sh
    echo "USER (Output from Bash): $USER"
    /usr/bin/python3.8 -c "import os; print('USER (Output from Python provided by Bash): $USER'); print('USER (Output from Python resolved from Python): {}'.format(os.environ['USER']))"

5) Powershell-script using environment variable and calling Python
    # test-env.ps1
    echo "USERNAME (Output from PowerShell): $env:USERNAME"
    & 'C:\Program Files\Python\3.6\python.exe' -c "import os; print('USERNAME (Output from Python provided from Powershell): $env:USERNAME'); print('USERNAME (Output from Python resolved from Python): {}'.format(os.environ['USERNAME']))"

