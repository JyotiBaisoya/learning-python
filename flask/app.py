from flask import Flask, request, jsonify

app = Flask(__name__)

data = {}  # Empty dictionary to store the data

@app.route('/')
def welcome():
    return 'Welcome to the Flask application!'

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

@app.route('/farewell/<username>')
def farewell(username):
    return f'Goodbye, {username}!'

@app.route('/create', methods=['POST'])
def create():
    json_data = request.get_json()
    key = json_data.get('key')
    value = json_data.get('value')
    if key and value:
        data[key] = value
        return jsonify({'message': 'Entry created successfully'})
    else:
        return jsonify({'message': 'Invalid request data'})

@app.route('/read', methods=['GET'])
def read():
    return jsonify(data)

@app.route('/update', methods=['POST'])
def update():
    json_data = request.get_json()
    key = json_data.get('key')
    value = json_data.get('value')
    if key in data:
        data[key] = value
        return jsonify({'message': 'Entry updated successfully'})
    else:
        return jsonify({'message': 'Entry not found'})

@app.route('/delete', methods=['POST'])
def delete():
    json_data = request.get_json()
    key = json_data.get('key')
    if key in data:
        del data[key]
        return jsonify({'message': 'Entry deleted successfully'})
    else:
        return jsonify({'message': 'Entry not found'})

if __name__ == '__main__':
    app.run()
