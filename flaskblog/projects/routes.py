from flask import (render_template, url_for, flash,
                    redirect, request, abort, Blueprint)


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
    return render_template('competitive.html', title="Competitive")