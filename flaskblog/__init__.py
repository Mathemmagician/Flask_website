from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

from flask_login import current_user


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	migrate.init_app(app, db)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from flaskblog.models import User, Post, Comment, Goat
	class MyModelView(ModelView):
	    def is_accessible(self):
	    	admins = User.query.filter_by(is_admin=1)
	    	return current_user in admins
	
	admin = Admin(app, name="Admin's Cave", template_mode='bootstrap3')
	admin.add_view(MyModelView(User, db.session))
	admin.add_view(MyModelView(Post, db.session))
	admin.add_view(MyModelView(Comment, db.session))
	admin.add_view(MyModelView(Goat, db.session))

	from flaskblog.users.routes import users
	from flaskblog.posts.routes import posts
	from flaskblog.main.routes import main
	from flaskblog.errors.handlers import errors
	from flaskblog.projects.routes import projects
	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(errors)
	app.register_blueprint(projects)

	return app

