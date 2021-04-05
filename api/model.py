from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'users'

    user_name = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User user_name={self.user_name} email={self.email}>'


class Project(db.Model):

    __tablename__ = 'projects'

    project_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = db.Column(db.String, db.ForeignKey('users.user_name'))
    project_type_id = db.Column(UUID(as_uuid=True), db.ForeignKey('project_types.project_type_id'))

    project_name = db.Column(db.String, nullable=False)
    project_description = db.Column(db.Text)
    project_create_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Project project_id={self.project_id} project_name={self.project_name}>'

class Entry(db.Model):

    __tablename__ = 'entries'

    entry_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = db.Column(UUID(as_uuid=True), db.ForeignKey('projects.project_id'))
    entry_type_id = db.Column(UUID(as_uuid=True), db.ForeignKey('entry_types.project_type_id'))
    quantity_type_id = db.Column(UUID(as_uuid=True), db.ForeignKey('quantity_types.quantity_type_id'))

    entry_quantity = db.Column(db.Integer, nullable=False)
    entry_note = db.Column(db.Text)
    entry_datetime = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Entry entry_id={self.entry_id} entry_quantity={self.entry_quantity}>'

class Project_Type(db.Model):

    __tablename__ = 'project_types'

    project_type_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_type_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Project_Type project_type_id={self.project_type_id} project_type_name={self.project_type_name}>'

class Entry_Type(db.Model):

    __tablename__ = 'entry_types'

    entry_type_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entry_type_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Entry_Type entry_type_id={self.entry_type_id} entry_type_name={self.entry_type_name}>'

class Quantity_Type(db.Model):

    __tablename__ = 'quantity_types'

    quantity_type_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quantity_type_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Quantity_Type pquantity_type_id={self.quantity_type_id} quantity_type_name={self.quantity_type_name}>'


def connect_to_db(flask_app, db_uri='postgresql:///writingstats', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
