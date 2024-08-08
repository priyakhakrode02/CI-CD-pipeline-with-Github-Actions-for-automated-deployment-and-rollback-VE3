from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_ve3():
    return 'Hello World, This is VE3 DevOps Assignment!!'

if __name__ == '__main__':
    app.run(debug=True)
