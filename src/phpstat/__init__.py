from flask import Flask
from DirWalker import DirWalker, DirPrinter

app = Flask(__name__)

@app.route('/')
def create_list():
    walker = DirWalker()
    printer = DirPrinter()
    walker.get_dir_info( '/var/www/extensions/Maps/' )
    return printer.prnt(walker.get_stats())

if __name__ == '__main__':
    app.run(debug=True)

