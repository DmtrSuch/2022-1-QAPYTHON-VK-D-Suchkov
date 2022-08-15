import threading


from flask import Flask, jsonify, request, make_response
import json

import settings

app = Flask(__name__)

users = {"Adminadmin": "555" }
id_seq = 1

def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })

    server.start()
    return server

def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()

@app.route('/vk_id/<username>', methods=['GET'])
def get_user(username):
    user_id = users.get(username, None)
    result = {}
    if user_id:
        result = {'vk_id': str(user_id)}
        res = make_response(result)
        res.headers['Status:'] = '200 OK'
        res.headers['Content-Type:'] = 'application/json'
        res.headers['Response:'] = result
        return res
    else:
        res = make_response(result)
        res.headers['Status:'] = '404 Not Found'
        res.headers['Content-Type:'] = 'application/json'
        res.headers['Response:'] = result
        return res

@app.route('/vk_id/add_user', methods=['POST'])
def create_user():
    global id_seq
    user_name = json.loads(request.data)['name']
    if user_name not in users:
        users[user_name] = id_seq
        data = {'user_id': str(id_seq)}
        id_seq += 1
        return jsonify(data), 201
    else:
        return jsonify(f'User name {user_name} in users: id {users[user_name]}'), 400


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200

if __name__ == '__main__':
    run_mock()