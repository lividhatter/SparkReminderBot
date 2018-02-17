from flask import Flask, jsonify, request

app = Flask(__name__)

messages = [{'from' : 'Cameron', 'message': 'this is the message'}]

@app.route('/')
def Homepage():
    return "Hello Livid!"

@app.route('/sparkbot/messages')
def get_messages():
    return jsonify(messages)


@app.route('/sparkbot/messages', methods=['POST'])
def send_message():
    messages.append(request.get_json())
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)