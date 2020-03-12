from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '23fb9d676097ee712ce5ee95d50f96ba'

posts = [
    {
        'author': "Ramil",
        'title': "First Blog",
        'content': "First sentence. Nice.",
        'date': "Mar 11, 2020"
    },
    {
        'author': "Markiza",
        'title': "Second Blog",
        'content': "wow sentence. Nice.",
        'date': "Mar 213, 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created form {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
    app.run(debug=True)
