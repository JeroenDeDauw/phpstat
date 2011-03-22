#from flask import Flask
from dirinfo import DirInfo
from dirprinter import repr_as_indented_list

#app = Flask(__name__)

#@app.route('/')
def create_list():
    return print_list()

def print_list():
    dir = DirInfo('/var/www/extensions/Maps/')
    return repr_as_indented_list(dir, 0)   

if __name__ == '__main__':
    print create_list()
    #app.run(debug=True)

