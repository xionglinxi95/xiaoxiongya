# -*- coding:utf-8 -*-
__author__ = 'liuxiaotong'

import dataset


class UserTokenDao:

    db = dataset.connect('mysql://root:12345678@localhost/get_start')

    @classmethod
    def create_token(cls, uid, token, expire_time):
        sql = 'insert into user_token (uid, token, expire_time) values (:uid, :token, :expire_time)'
        params = {
            'uid': uid,
            'token': token,
            'expire_time': expire_time,
        }
        cls.db.query(sql, params)

    @classmethod
    def get_token_info(cls, token):
        res = cls.db.query('select * from user_token where token = :token;', {"token": token})
        res = [dict(item) for item in res]
        if res:
            return res[0]
        return None

    @classmethod
    def delete_token_info(cls, token):
        cls.db.query('delete from user_token where token = :token;', {"token": token})
