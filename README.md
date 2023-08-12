# 0x00. AirBnB clone - The console
This is a command-line interpreter that enables users to enter command with arguments (whenever necessary) to perform special tasks. Users get to create objects using this tool, manipulate the already existing objects, retrieve details on exisiting as well and delete objects which are created.

This directory contains source code files on the AirBnB clone console project. This project was created as part of our course requirement at ALX.

## Features
This project is a command-line interpreter that enables users to perform some defined operations. The core features would be to manage objects in this project like:
* Creating new objects (Users and Places)
* Persisting created objects into files
* Retrieving objects from files
* Manipulating retrieved objects
* Updating attributes of an object
* Destroying an object
* Autocompletion of commands

## Concepts
* Python packages and modules
* datetime module
* uuid module
* TDD using unittest module
* args & kwargs
* cmd module

## Prerequisites
This tool can be run on the following platforms (OS):
* Windows
* Ubuntu
* MacOS

The following software(s) has to be installed in other to execute this command-line tool:
* Python 3.8.5 (or newer) [Download](https://www.python.org/downloads/)


## How To's
### Starting the command-line interpreter
The command-line tool can be started from any terminal on any of the supported OS. Use the following snippet to start the program in the interactive mode:

`./console.py`

This will start the command-line interface showing a prompt. This signals that the tool is ready to process the commands the user provides infinitely until the user chooses to end the session.

The tool can also be started in the non-interactive mode using the following snippet:

`echo "help" | ./console.py`

### Using the command-line interpreter
After starting the tools you can perform diverse operations directly from the command-line interface.
You can type `help` to see a list of all the available commands. You can also obtains information on how to use any of the listed commands using the following snippet:

`help command_name`

### Examples
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
create  help	add  change  quit

Undocumented commands:
======================
(hbnb) help create
```
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```
