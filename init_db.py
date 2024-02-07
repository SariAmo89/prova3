# In Terminal 'flask shell < init_db.py'
from ThermoSoftware import db
from ThermoSoftware.models import Role, User

# Lösche die bisherige Datenbank
db.drop_all()

# Create neue
db.create_all()

# Create Function for Role
def find_or_create_role(id, name):
    """ Find existing role or create new role """
    role = Role.query.filter(Role.name == name).first()
    if not role:
        role = Role(id=id, name=name)
        db.session.add(role)
    return role

# Create Role
db.session.add(Role(id=1, name="Admin"))
db.session.add(Role(id=2, name="User"))
db.session.commit()

# Create Function for User
def find_or_create_user(username, email, password, role):
    """ Find existing user or create new user """
    user = User.query.filter(User.email == email).first()
    if not user:
        user = User(email=email,
                    username=username,
                    password=password)
        if role:
            user.roles.append(role)
        db.session.add(user)
    return user

# Adding roles
admin_role = find_or_create_role(1, 'Admin')

# Adding Users
user = find_or_create_user(u'Admin', u'admin@example.com', 'Password1', admin_role)

# Commiting everything
db.session.commit()





