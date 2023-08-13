#!/usr/bin/python3
"""
Defines a module that created the command-line
interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ Define the command-line interpreter """

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Place",
                     "State", "City", "Amenity",
                     "Review"]

    def do_quit(self, arg):
        """ A handler to quit the interpreter """
        return (True)

    def help_quit(self):
        """
        The handler for providing help for the quit command
        """
        self.exit_helper_text()

    def do_EOF(self, arg):
        """ A handler to Ctrl + D signal """
        return (True)

    def help_EOF(self):
        """
        The handler for providing help for the EOF command
        """
        self.exit_helper_text()

    def emptyline(self):
        """ A handler for emptylines """
        pass

    def postloop(self):
        """ Handler called to end command line loop """
        print()

    def exit_helper_text(self):
        """
        Prints the instructions for the quit and
        EOF commands when the help utility
        is invoked
        """
        print("Quit the command-line interface\n")

    @staticmethod
    def validate_arg(caller, arg):
        """
        Validates the arguments passed to a command

        Parameters:
        caller : string
            The command handler whose arguments need
            to be validated
        arg : string
            The arguments for the command

        Returns
            The value 1 when there's an error with
            the command's syntax provided provided
            by the user. 0 is returned to indicate
            a valid syntax
        """
        messages = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** attribute name missing **",
                    "** value missing **"]

        if (arg == "" and caller != "all"):
            print(messages[0])
            return (1)
        if (arg not in HBNBCommand.valid_classes and
           caller == "create"):
            print(messages[1])
            return (1)
        if (arg != "" and caller == "all" and arg not in
           HBNBCommand.valid_classes):
            print(messages[1])
            return (1)
        if (caller != "all" and arg.split()[0] not in
           HBNBCommand.valid_classes and (caller == "show"
           or caller == "destroy" or caller == "update")):
            print(messages[1])
            return (1)
        if (len(arg.split()) == 1 and (caller == "show" or
           caller == "destroy" or caller == "update")):
            print(messages[2])
            return (1)
        if (len(arg.split()) == 2 and caller == "update"):
            print(messages[3])
            return (1)
        if (len(arg.split()) == 3 and caller == "update"):
            print(messages[4])
            return (1)
        return 0

    def do_create(self, arg):
        """
        A handler to save a new instance of BaseModel after
        creation
        """
        if (HBNBCommand.validate_arg("create", arg) == 1):
            return (None)
        obj = eval(arg + "()")
        obj.save()
        print(obj.id)

    def help_create(self):
        """
        The handler for providing help for the create
        command
        """
        print("Create a new instance of BaseModel then "
              "save it to a file displaying the ID for "
              "the newly created object. Syntax: create "
              "<class_name>\n")

    def do_show(self, arg):
        """
        A handler to print details for a given instance
        """
        objects = {}
        key = ""
        file_obj = None

        if (HBNBCommand.validate_arg("show", arg) == 1):
            return (None)

        file_obj = FileStorage()
        objects, key = HBNBCommand.load_objects(arg, file_obj)
        if (objects is None):
            return (None)

        print(objects.get(key))

    def help_show(self):
        """
        The handler for providing help for the show
        command
        """
        print("Prints a given instance based on the "
              "class name and an ID. Syntax: show "
              "<class_name> <ID>\n")

    @staticmethod
    def load_objects(arg, file_obj):
        """
        Loads all the saved data into a local
        cache

        Parameters
        arg : string
            The arguments for the command. It
            contains the model name and ID
        file_obj : class<FileStorage>
            An instance of the file storage to
            manipulate the data stored

        Return
            A tuple made of all the objects stored
            and a key formed from the argument.The
            key might not be used by some callers
            """
        args = []
        key = ""
        objects = {}

        args = arg.split()
        objects = file_obj.all()
        key = f"{args[0]}.{args[1]}"
        if (key not in tuple(objects.keys())):
            print("** no instance found **")
            return (None, None)

        return (objects, key)

    def do_destroy(self, arg):
        """ A handler to delete an instance """
        objects = {}
        key = ""
        file_obj = None

        if (HBNBCommand.validate_arg("destroy", arg) == 1):
            return (None)

        file_obj = FileStorage()
        objects, key = HBNBCommand.load_objects(arg, file_obj)
        if (objects is None):
            return (None)

        del objects[key]
        file_obj.save()

    def help_destroy(self):
        """
        The handler for providing help for the destroy
        command
        """
        print("Deletes an instance based on the class "
              "name and an ID. Syntax: destroy "
              "<class_name> <ID>\n")

    def do_all(self, arg):
        """ A handler to print all instances """
        objects = {}
        found_objects = []

        if (HBNBCommand.validate_arg("all", arg) == 1):
            return (None)

        objects = FileStorage().all()
        for key, value in objects.items():
            if (arg != "" and arg in key):
                found_objects.append(str(value))
            elif (arg == ""):
                found_objects.append(str(value))

        print(found_objects)

    def help_all(self):
        """
        The handler for providing help for the all
        command
        """
        print("Prints all the instances created. Syntax: "
              "all [<class_name>]. When <class_name> is "
              "provided only classes with the given name "
              "will be displayed\n")

    def do_update(self, arg):
        """
        A handler to update attributes for an
        instance
        """
        model_name, id, attribute, value = "", "", "", ""
        objects = {}
        file_obj = None

        if (HBNBCommand.validate_arg("update", arg) == 1):
            return (None)

        model_name, id, attribute, value = arg.split()[0:4]
        file_obj = FileStorage()
        objects, key = HBNBCommand.load_objects(arg, file_obj)
        if (objects is None):
            print("** no instance found **")
            return (None)
        if ("\"" in value):
            value = HBNBCommand.build_str(arg)
        elif ("." in value):
            value = float(value)
        else:
            value = int(value)
        setattr(objects.get(key), attribute, value)
        file_obj.save()

    def help_update(self):
        """
        The handler for providing help for the
        update command
        """
        print("Updates the attribute for an instance one at "
              "a time. Adds the attribute if it does not "
              "exist or tries to update already existing "
              "attributes. Syntax: update <class_name> <ID> "
              "<attribute_name> <value>")

    @staticmethod
    def build_str(arg):
        """
        Builds a string from values found in
        quotations from the given argument

        Parameters
        arg : string
            The argument contains characters
            to build the string

        Return
            The string found between a pair of
            quotations
        """
        temp = []
        increment = 3
        value = ""

        temp = arg.split()
        while (increment < len(temp)):
            value += temp[increment]
            if (temp[increment].endswith("\"")):
                break
            value += " "
            increment += 1

        return (value[1:-1])

    def default(self, arg):
        """
        Defines the behaviour for unknown commands.
        This also ensures that the behaviour of
        our CLI is adjusted retrieve objects for
        a given class
        """
        valid_suffix = ["all()", "count()"]
        prefix_str, suffix_str, id = "", "", ""
        objects = {}
        found_objects = []

        if ("." in arg):
            prefix_str = arg.split(".")[0]
            suffix_str = arg.split(".")[1]

            if (prefix_str in HBNBCommand.valid_classes and
               suffix_str in valid_suffix or
               suffix_str.startswith("show(\"") or
               suffix_str.startswith("destroy(\"")):
                if (suffix_str == "all()"):
                    HBNBCommand.print_all_class_instances(prefix_str)
                elif (suffix_str == "count()"):
                    HBNBCommand.print_instance_count(prefix_str)
                elif (suffix_str.startswith("show(\"") and
                      suffix_str.endswith("\")")):
                    id = suffix_str[6:-2]
                    HBNBCommand.print_instance_using_id(prefix_str, id)
                elif (suffix_str.startswith("destroy(\"") and
                      suffix_str.endswith("\")")):
                    id = suffix_str[9:-2]
                    HBNBCommand.destroy_instance_using_id(prefix_str, id)

                return (None)

        return (cmd.Cmd.default(self, arg))

    @staticmethod
    def filter_objects(class_name, id=""):
        """
        Returns a list of objects for the given
        class.

        Parameters
        class_name : string
            The name of the class used in filtering
            the objects to be displayed
        id : string, optional
            The ID for the search object. The
            default value is an empty string

        Return
            A list of objects matching whose classes
            match the given class name
        """
        objects = {}
        found_objects = []

        objects = FileStorage().all()

        for key, value in objects.items():
            if (class_name in key):
                if (id != "" and id == value.id):
                    found_objects.append(str(value))
                    break
                elif (id != ""):
                    continue
                found_objects.append(str(value))

        return (found_objects)

    @staticmethod
    def print_all_class_instances(class_name):
        """
        Prints all the instances for a class

        Parameters
        class_name : string
            The name of the class used to invoke the
            all command. This class will be used
            in filtering the objects to be displayed
        """
        print(HBNBCommand.filter_objects(class_name))

    @staticmethod
    def print_instance_count(class_name):
        """
        Prints the total number of instances for
        a class

        Parameters
        class_name : string
            The name of the class used to invoke the
            count command. This class will be used
            in filtering the objects to be displayed
        """
        print(len(HBNBCommand.filter_objects(class_name)))

    @staticmethod
    def print_instance_using_id(class_name, id):
        """
        Print the instance with the given ID

        Parameters
        class_name : string
            The name of the class used to invoke the
            show command. This class will be used
            in filtering the objects to be displayed
        id : string
            The ID for the given object
        """
        object = HBNBCommand.filter_objects(class_name, id)
        if (object == []):
            print("** no instance found **")
        else:
            print(object)

    @staticmethod
    def destroy_instance_using_id(class_name, id):
        """
        Deletes the instance with the given ID

        Parameters
        class_name : string
            The name of the class used to invoke the
            destroy command. This class will be used
            in filtering the objects to be deleted
        id : string
            The ID for the given object
        """
        object = HBNBCommand.filter_objects(class_name, id)
        if (object == []):
            print("** no instance found **")
        else:
            file_obj = FileStorage()
            objects = file_obj.all()
            key = f"{class_name}.{id}"
            del objects[key]
            file_obj.save()


if (__name__ == "__main__"):
    HBNBCommand().cmdloop()
