# -*- coding:utf-8 -*-
__author__ = 'liuxiaotong'
from flask import Flask, request, make_response, redirect, render_template

from service.user import UserService

app = Flask(__name__)
host = "127.0.0.1"
port = 8082


@app.route('/xiong', methods=['GET'])
def hello_world():
    return 'hello, meng!'


@app.route('/', methods=['GET'])
def welcome():
    token = request.cookies.get('token')
    if token:
        user = UserService.get_user_info(token)
    else:
        user = {}
    return render_template('welcome.html', user=user)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        expire_time = 7*24*60*60
        user = UserService.register(username, password, expire_time)
        resp = make_response(redirect('/', '302'))
        resp.set_cookie('token', user['token'])
        return resp
    elif request.method == 'GET':
        return render_template('register.html')


@app.route('/logout', methods=['GET'])
def logout():
    token = request.cookies.get('token')
    UserService.delete_token_info(token)
    resp = make_response(redirect('/', '302'))
    resp.delete_cookie('token')
    return resp


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        expire_time = 7*24*60*60
        user = UserService.login(username, password, expire_time)
        resp = make_response(redirect('/', '302'))
        resp.set_cookie('token', user['token'])
        return resp
    elif request.method == 'GET':
        return render_template('login.html')


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
