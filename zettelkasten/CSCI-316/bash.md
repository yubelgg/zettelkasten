---
id: bash
aliases: []
tags:
  - regex
---

# Bash

`cat` command will print text file to the terminal

To create a script with bash you create a file with `.sh` as the extension
Inside you can commands like `echo hello world!`

- to run `bash filename.sh`
  - will print to console `hello world!`
- you can provide the file with the interpreter you wish to use
  - `#!/bin/bash` <- the **FULL** path of $SHELL
  - you have to grant permission to file to execute `./filename.sh`
    - `chmod u+x filename.sh` <- grants this user to execute

## Creating a script

You can create variables.
To use the variable you call by adding $ before the variable name.

Getting inputs:
use `read variable_name`

## Piping

sending command output to another command.

Example:
`ls -l /usr/bin | grep bash`
This provides a list of only directorys in /usr/bin that has bash

Appending output to a file:
`>` writes to a file

- `echo hello world! > hello.txt` will contain text hello world
- will override text each time, if file exist

`>>` will append to a file:

- `echo hello world! >> hello.txt` will contain 2 lines of hello world

## Conditions

[] are used for test/conditions

```bash
if []; then
elif [];then
else
fi
```

### Arrays

Arrays are defined in () and each element seperated by a space
`echo my_list` will return the first value
`echo ${my_list[@]}` will return all values, replace @ for position you want

### for loop

```bash
for item in ${my_list[@]}; do
    echo -n $item | wc -c; done
```

-n will ignore new line
wc -c for word count

### Functions

```bash
myfunc() {
    //code
}
myfunc
```

## SED

replace text in a file in the cli using [[regex-and-cfg|regular expression]]
