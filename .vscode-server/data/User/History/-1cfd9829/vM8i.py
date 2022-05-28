from flask import Flask         #from the flask module import the Flask class. This is an import statement. 
                                #Google: An import statement tells the compiler the path of a class or the entire package.

#OOP-> object oriented programming
app = Flask(__name__)             #Instantiating our Flask class into app (object). This is an instance, an instance is an object that belongs to a class.                        
                                #Classes are blueprints. Class is to object like blueprint is to house. A method is a function that belongs to a class. 


@app.get("/")                   #A decorator that allows us to map routes to view functions. A decorator starts with @. 
def index():                    # Our view function.
    me = {                      # me is a variable containing a dictionay (a special python data structure). Curly braces in python = dictionary.
        "first_name": "Victoria",
        "last_name": "Warren",
        "hobbies": "Fitbit"
    }

    return me                   # when we return a dictionary from a view function in flask,
                                # it is automatically converted into JSON

#JSON stands for javascript objection notation, defintion: JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. 
