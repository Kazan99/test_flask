from flask import Flask, render_template

app = Flask(__name__);

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new')
def img_new():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug= True);
