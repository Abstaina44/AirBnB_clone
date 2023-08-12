#!/usr/bin/python3
"""
Defines a module that created the command-line
interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Define the command-line interpreter """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        A handler to quit the interpreter
        
        Parameters
        arg : string
            The argument passed to this command
        """
        return (True)

    def help_quit(self):
        """
        The handler for providing help for the quit command
        """
        self.exit_helper_text()

    def do_EOF(self, arg):
        """
        A handler to Ctrl + D signal

        Parameters
        arg : string
            The argument passed to this command
        """
        return (True)

    def help_EOF(self):
        """
        The handler for providing help for the EOF command
        """
        self.exit_helper_text()

    def emptyline(self):
        """ A handler for emptylines """
        pass

    def exit_helper_text(self):
        """
        Prints the instructions for the quit and
        EOF commands when the help utility
        is invoked
        """
        print("Quit the command-line interface\n")


if (__name__ == "__main__"):
    HBNBCommand().cmdloop()
