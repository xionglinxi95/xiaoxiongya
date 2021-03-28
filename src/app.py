# -*- coding:utf-8 -*-
__author__ = 'xiongmeng'
from flask import Flask, request, make_response, redirect, render_template

from service.user import UserService
from service.note import NoteService

app = Flask(__name__)
host = "0.0.0.0"
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


@app.route('/note', methods=['POST', 'GET'])
def note():
    # 获取当前token
    token = request.cookies.get('token')

    if token:
        # 根据token获取user_id
        uid = UserService.get_user_id_by_token(token)
        # user = UserService.get_user_info(token)
        # uid = user.get('uid')
        # 根据user_id 获取note_list
        note_list = NoteService.get_note_list(uid)
        return render_template('note_list.html', note_list=note_list)
    else:
        resp = make_response(redirect('/login', '302'))
        return resp


@app.route('/note/<int:note_id>', methods=['POST', 'GET'])
def note_detail(note_id):
    token = request.cookies.get('token')
    if token:
        # 根据token获取user_id
        uid = UserService.get_user_id_by_token(token)
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            NoteService.update_note_info(note_id, uid, title, content)
            resp = make_response(redirect(f'/note/{note_id}', '302'))
            return resp
        elif request.method == 'GET':
            # 通过note_id, user_id查看当前笔记
            note_info = NoteService.get_note_info(note_id, uid)
            return render_template('note_info.html', note_info=note_info)
    else:
        resp = make_response(redirect('/login', '302'))
        return resp


@app.route('/note/<int:note_id>/delete', methods=['POST'])
def note_delete(note_id):
    token = request.cookies.get('token')
    if token:
        # 根据token获取user_id
        uid = UserService.get_user_id_by_token(token)
        if request.method == 'POST':
            NoteService.delete_note_info(note_id, uid)
            resp = make_response(redirect('/note', '302'))
            return resp
    else:
        resp = make_response(redirect('/login', '302'))
        return resp


@app.route('/note/new', methods=['POST', 'GET'])
def note_new():
    token = request.cookies.get('token')
    if token:
        # 根据token获取user_id
        uid = UserService.get_user_id_by_token(token)
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            NoteService.create_note_info(uid, title, content)
            resp = make_response(redirect('/note', '302'))
            return resp
        elif request.method == 'GET':
            # 通过note_id, user_id查看当前笔记
            note_info = {}
            return render_template('note_info.html', note_info=note_info)
    else:
        resp = make_response(redirect('/login', '302'))
        return resp


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
