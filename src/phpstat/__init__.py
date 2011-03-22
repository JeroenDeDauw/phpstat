from flask import Flask
from DirInfo import DirInfo
from DirPrinter import repr_as_indented_list

app = Flask(__name__)

@app.route('/')
def create_list():
    #printer = DirPrinter()
    dir = DirInfo('/var/www/extensions/Maps/')
    return repr_as_indented_list(dir, 0)

if __name__ == '__main__':
    app.run(debug=True)

