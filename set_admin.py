
from flaskblog import create_app, db
from flaskblog.models import User

app = create_app()
app.app_context().push()

user = User.query.filter_by(email="ramil9898@gmail.com").first()
assert user == User.query.first()

user.is_admin = 1

db.session.commit()
