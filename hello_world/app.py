from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from models import User, Posts
from database import Database

app = Flask(__name__)
Bootstrap(app)
database = Database()

@app.route('/')
def index():
    title = 'Home'
    posts = database.return_posts()
    return render_template('index.html', title=title, posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Register'
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password_c = request.form['password_c']
        if password == password_c:
            user = User(name,surname,email,username,password)
            database.create_user(user)
            return render_template('register.html', title=title)
        else:
            return render_template('bean.html', title='Beaned It')
        
    return render_template('register.html', title=title)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    title = 'Create Post'
    if request.method == 'POST':
        title = request.form['title']
        subheading = request.form['subheading']
        image = request.form['image']
        description = request.form['description']
        post = Posts('baysicinglish', title, subheading, image, description)
        database.create_post(post)
    return render_template('create_post.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)