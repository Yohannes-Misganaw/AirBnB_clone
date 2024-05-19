import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it and prints the id"""
        if arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Show an instance based on class name and id"""
        args = arg.split()
        if len(args) < 2:
            print("** class name or id missing **")
        else:
            # Logic to retrieve the instance and display it

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_EOF(self, arg):
        """End of File"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
