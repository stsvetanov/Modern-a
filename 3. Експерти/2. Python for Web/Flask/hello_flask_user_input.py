from flask import Flask, request

app = Flask(__name__)


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    else:
        name = request.args.get('name')
        return f'Hello, {name}!'


if __name__ == '__main__':
    app.run()
