from flask import (render_template, url_for, flash,
                    redirect, request, abort, Blueprint)
from flaskblog.main.utils import get_codeforces_rating, create_figure
from flask_login import current_user, login_required
from flaskblog.projects.forms import GoatForm
from flaskblog.models import Goat
from flaskblog import db


projects = Blueprint('projects', __name__, template_folder='project_templates', 
	url_prefix='/projects', static_folder='static')


@projects.route("/academic")
def academic():
    return render_template('academic.html', title="Academic")


@projects.route("/development")
def development():
    return render_template('development.html')


@projects.route("/competitive")
def competitive():
    return render_template('competitive.html', title="Competitive", codeforces=True)


@projects.route("/goat")
def goat():
	goats = Goat.query.order_by(Goat.score.desc()).all()
	goats = [goat.__dict__ for goat in goats]
	for goat in goats:
		goat.pop('_sa_instance_state', None)

	return render_template('goat.html', title="Greatest of All Time", goats=goats)


@projects.route("/goat/new", methods=['GET', 'POST'])
@login_required
def new_goat():
    if not current_user.is_admin:
        abort(403)
    form = GoatForm()
    if form.validate_on_submit():
        goat = Goat(name=form.name.data, info=form.info.data, 
        	score=form.score.data, image_url=form.image_url.data)
        db.session.add(goat)
        db.session.commit()
        flash('Goat has been created', 'success')
        return redirect(url_for('projects.goat'))
    return render_template('new_goat.html', title='New Goat', 
        form=form, legend="New Goat")


