from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    string = 'roman is in the house'
    return 'Hello World! {}'.format(string)



if __name__ == '__main__':
    app.run()
