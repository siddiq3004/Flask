from flask import render_template,flash,url_for,redirect
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog import app
# with app.app_context():
#     db.create_all()


posts = [
    {
    'author' :'siddiq',
    'title' : 'Blog 1',
    'content' : 'one content',
    'date_posted' : '06 April,2023'
    },
    {
    'author' :'shaik',
    'title' : 'Blog 2',
    'content' : 'Two content',
    'date_posted' : '05 April,2023'
    }
]
# Create Flask object
'''Routes in a Flask app can be created by defining 
a view function and associating a URL with it using the route() decorator. '''
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)
    # return '<h1> Home Page<h1/>' # Output: The text `Hello, World!` is displayed at the URL path '/'
@app.route('/about')
def About():
    return render_template('about.html',title='About')
    # return '<h1> About Page<h1/>'
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account is created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)
    
    # return '<h1> About Page<h1/>'
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@blog.com' and form.password.data =='password':
            flash('You have been logged In','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. please check username and password','danger')
    return render_template('login.html',title='Login',form = form)
    # return '<h1> About Page<h1/>'