# -*- coding: utf-8 -*-
__auth__ = "timbby"

import dataset


class ConnectMySQL:
    def __init__(self, db_url):
        self.db = dataset.connect(db_url)
        self.user_info = self.db.user_info

    def walk(self, sql):
        return self.db.query(sql)

    def sleep(self, sql):
        return self.db.query(sql)


get_start_db = ConnectMySQL('mysql://root:12345678@127.0.0.1/get_start')
