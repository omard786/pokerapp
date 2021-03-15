from flask import Flask

app = Flask(__name__)

@app.route('home')
def hello_internet():
    return "Hello Internet!"

if __name__=='__main__':
    app.run(debug=True)

@app.route()