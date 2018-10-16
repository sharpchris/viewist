from app import db

class Link(db.Model):

    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True)
    subdomain = db.Column(db.String(128), db.ForeignKey('account.subdomain'))
    destination = db.Column(db.String(2048))
    tracking_link = db.Column(db.String(2048))
    create_datetime = db.Column(db.DateTime())
    last_view_datetime = db.Column(db.DateTime())
    count_views = db.Column(db.SmallInteger)

class Account(db.Model):

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    subdomain = db.Column(db.String(128))
    create_datetime = db.Column(db.DateTime())
    is_active = db.Boolean()

