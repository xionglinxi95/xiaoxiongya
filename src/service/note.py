# -*- coding: utf-8 -*-
__auth__ = "xiaoxiongya"

from dao.note import NoteDao


class NoteService:
    @classmethod
    def get_note_list(cls, uid):
        note_list = NoteDao.get_note_list(uid)
        return note_list

    @classmethod
    def get_note_info(cls, nid, uid):
        note_info = NoteDao.get_note_info(nid, uid)
        return note_info

    @classmethod
    def update_note_info(cls, nid, uid, title, content):
        NoteDao.update_note_info(nid, uid, title, content)

    @classmethod
    def create_note_info(cls, uid, title, content):
        NoteDao.create_note_info(uid, title, content)

    @classmethod
    def delete_note_info(cls, nid, uid):
        NoteDao.delete_note_info(nid, uid)



