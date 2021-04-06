from model import db, User, Project, Entry, Project_Type, Entry_Type, Quantity_Type, connect_to_db

def create_user(user_name, email, password):

    user = User(user_name=user_name, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    return User.query.all()

def get_user_by_name(user_name):
    return User.query.get(user_name)

def create_project(user, project_type, project_name, project_description, project_create_date):

    project = Project(user=user,
                  project_type=project_type,
                  project_name=project_name,
                  project_description=project_description,
                  project_create_date=project_create_date)

    db.session.add(project)
    db.session.commit()

    return project

def get_projects():
    return Project.query.all()

def get_project_by_id(project_id):
    return Project.query.get(project_id)

def create_entry(project, entry_type, quantity_type, entry_quantity, entry_note, entry_datetime):

    entry = Entry(project=project,
                entry_type=entry_type,
                quantity_type=quantity_type,
                entry_quantity=entry_quantity,
                entry_note=entry_note,
                entry_datetime=entry_datetime)

    db.session.add(entry)
    db.session.commit()

    return entry

def get_entries():
    return Entry.query.all()

def get_entry_by_id(entry_id):
    return Entry.query.get(entry_id)

def create_project_type(project_type_name):

    project_type = Project_Type(project_type_name=project_type_name)

    db.session.add(project_type)
    db.session.commit()

    return project_type

def get_project_types():
    return Project_Type.query.all()

def get_project_type_by_id(project_type_id):
    return Project_Type.query.get(project_type_id)

def create_entry_type(entry_type_name):

    entry_type = Entry_Type(entry_type_name=entry_type_name)

    db.session.add(entry_type)
    db.session.commit()

    return entry_type

def get_entry_type():
    return Entry_Type.query.all()

def get_entry_type_by_id(entry_type_id):
    return Entry_Type.query.get(entry_type_id)

def create_quantity_type(quantity_type_name):

    quantity_type = Quantity_Type(quantity_type_name=quantity_type_name)

    db.session.add(quantity_type)
    db.session.commit()

    return quantity_type

def get_quantity_type():
    return Quantity_Type.query.all()

def get_quantity_type_by_id(quantity_type_id):
    return Quantity_Type.query.get(quantity_type_id)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)