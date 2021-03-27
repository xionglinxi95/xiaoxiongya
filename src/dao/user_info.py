# -*- coding:utf-8 -*-
__author__ = 'liuxiaotong'

import dataset


# data access object
class UserInfoDao:
    #                     协议     账号  密码     ip   : 端口 / db_name
    db = dataset.connect('mysql://root:12345678@localhost/get_start')

    @classmethod
    def get_by_username(cls, send_name):
        res = cls.db.query('select * from user_info where username = :username1;', {"username1": send_name})
        res = [dict(item) for item in res]
        if res:
            return res[0]
        return None

    @classmethod
    def get_by_uid(cls, uid):
        res = cls.db.query('select * from user_info where uid = :uid;', {"uid": uid})
        res = [dict(item) for item in res]
        if res:
            return res[0]
        return None

    @classmethod
    def create_user(cls, username, password):
        sql = 'insert into user_info (username, password) values (:username, :password)'
        params = {
            'username': username,
            'password': password,
        }
        cls.db.executable.execute(sql, params)


if __name__ == '__main__':
    res = UserInfoDao.get_by_uid(1)
    print(res)
