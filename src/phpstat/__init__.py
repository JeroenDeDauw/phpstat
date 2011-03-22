#from flask import Flask
from dirinfo import DirInfo
from dirprinter import DirPrinter

#app = Flask(__name__)

#@app.route('/')
def print_list():
    printer = DirPrinter()
    return printer.prnt(DirInfo('/var/www/extensions/Maps/'))   

if __name__ == '__main__':
    print print_list()
    #app.run(debug=True)