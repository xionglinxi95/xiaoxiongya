# -*- coding: utf-8 -*-
__auth__ = "xiaoxiongya"

import dataset


class NoteDao:
    #                     协议     账号  密码     ip   : 端口 / db_name
    db = dataset.connect('mysql://root:12345678@localhost/get_start')

    @classmethod
    def get_note_list(cls, uid):
        res = cls.db.query('select * from note where uid = :uid1;', {"uid1": uid})
        res = [dict(item) for item in res]
        return res

    @classmethod
    def get_note_info(cls, nid, uid):
        res = cls.db.query('select * from note where id =:nid and uid = :uid1;', {"nid": nid, "uid1": uid})
        res = [dict(item) for item in res]
        if res:
            return res[0]
        return None

    @classmethod
    def update_note_info(cls, nid, uid, title, content):
        cls.db.query(
            'update note set title=:title1, content=:content1 where id =:nid and uid = :uid1',
            {"title1": title, "content1": content, "nid": nid, "uid1": uid}
        )

    @classmethod
    def create_note_info(cls, uid, title, content):
        sql = 'insert into note (title, content, uid) values (:title, :content, :uid)'
        params = {
            'title': title,
            'content': content,
            'uid': uid,
        }
        cls.db.query(sql, params)

    @classmethod
    def delete_note_info(cls, nid, uid):
        cls.db.query('DELETE from note where uid = :uid and id = :nid', {"uid": uid, 'nid': nid})





