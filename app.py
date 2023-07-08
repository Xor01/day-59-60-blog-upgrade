from flask import Flask, render_template
from requests import get
from dotenv import load_dotenv
from os import getenv
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/post.html')
def post():

    blog_posts = get(url=getenv('POSTS_API')).json()
    return render_template('post.html', posts=blog_posts)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
    load_dotenv()
