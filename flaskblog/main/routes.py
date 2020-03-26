from flask import render_template, request, Blueprint, flash, redirect, url_for
from flaskblog.models import Post
from flaskblog.main.forms import ContactForm
from flaskblog.main.utils import send_contact_email


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', sidebar=True)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts, sidebar=True)

@main.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
    	eemail = form.email.data
    	ttitle = form.title.data
    	bbody  = form.content.data
    	send_contact_email(eemail, ttitle, bbody)
    	flash("Message sent! I'll get back to it as soon as possible!", "success")
    	return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', form=form)

