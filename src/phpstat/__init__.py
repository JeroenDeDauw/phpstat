from flask import Flask
from DirWalker import DirWalker

app = Flask(__name__)

@app.route('/')
def create_list():
    walker = DirWalker()
    
    return walker.walk()

if __name__ == '__main__':
    app.run(debug=True)

