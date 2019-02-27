from admin import db


class Hostgroup(db.Model):
    groupid = db.Column(db.String)
    name = db.Column(db.String)


class Host(db.Model):
    hostid = db.Column(db.String)
    host = db.Column(db.String)
