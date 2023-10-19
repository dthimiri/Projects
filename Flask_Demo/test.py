from flask import Flask, request, jsonify

app = Flask(__name__)

# decorator
@app.route('/add', methods = ['GET','POST'])
def add():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        print(a+b)
        return jsonify(str(result))


@app.route('/sub', methods = ['GET','POST'])
def sub():
    if (request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a - b
        print(a-b)
        return jsonify(str(result))

@app.route('/mul', methods = ['GET','POST'])
def mul():
    if (request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a * b
        print(a*b)
        return jsonify(str(result))

@app.route('/div', methods = ['GET','POST'])
def div():
    if (request.method == 'POST'):
        a = request.json['num7']
        b = request.json['num8']
        result = a / b
        print(a/b)
        return jsonify(str(result))

if __name__ == "__main__":

    app.run()
