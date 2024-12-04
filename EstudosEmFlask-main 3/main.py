from estudo import app


if __name__ == '__main__':
    app.run(debug=True)


'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'minha Pagina'

if __name__ == '__main__':
    app.run(debug=True)

'''