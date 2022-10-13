# **AirBnB_clone v1 :sunny: - File storage / Console - with :snake: Python**

We made this project in order to learn how to recreate the AirBnB website, from the back-end data management to the front-end user interface.

This repo contains the first part of the project which consists in :

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage
- create all unittests to validate all our classes and storage engine

![Alt text](https://imagizer.imageshack.com/v2/1257x669q90/924/Aebfet.png "The part of this project: v1")

# **Command interpreter**

[**console.py**](console.py) - is used as the "entry-point" of the command-interpreter, here's the list of available commands:
    - **EOF** - exits the console <br>
    - **quit** - quit the console <br>
    - **emptyline** - emptyline method is here overloaded, in order to do nothing when you press enter <br>
    - **create** - Creates a new instance based on user input <br>
    - **show** - Prints the string representation of an instance, format \<classname\> \<id\> <br>
    - **destroy** - Deletes an instance and save modifications on the JSON file <br>
    - **all** - Prints all string representation of all instances based on the class name or not <br>
    - **update** - Updates an instance, based on class name and id provided by user, by adding or updating attributes <br> 

### **Mandatory part**


yet to be defined...

### Advanced part

yet to be defined...

## Installation

    yet to be defined...

## How to use it

<u>You can access the console via two modes.</u>

**Interactive mode:**

    $ ./console.py

**Non-interactive mode:**

    $ echo "<command>" | ./console.py

## **Examples**

**Standard commands:**
```
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create BaseModel
014ae95d-91b5-4c85-acc4-8d768482d471
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 014ae95d-91b5-4c85-acc4-8d768482d471
[BaseModel] (014ae95d-91b5-4c85-acc4-8d768482d471) {'created_at': datetime.datetime(2022, 10, 13, 5, 14, 44, 854946), 'updated_at': datetime.datetime(2022, 10, 13, 5, 14, 44, 855166), 'id': '014ae95d-91b5-4c85-acc4-8d768482d471'}
```


### Advanced commands:

        yet to be defined...

### Authors

- [Anthony Pizzonie](https://github.com/HINKOKO?tab=repositories)

- [Fabien Pineau](https://github.com/NekodaMushi)
