from flask import Flask
from DirWalker import DirWalker

app = Flask(__name__)

@app.route('/')
def create_list():
    walker = DirWalker()
    walker.walk( '/var/www/extensions/Maps/' )
    return walker.get_stats()

if __name__ == '__main__':
    app.run(debug=True)

