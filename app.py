from flask import Flask, render_template
from requests import get
from dotenv import load_dotenv
from os import getenv
app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    blog_posts = get(url=getenv('POSTS_API')).json()
    return render_template('index.html', posts=blog_posts)


@app.route('/post.html')
def show_all_posts():
    blog_posts = get(url=getenv('POSTS_API')).json()
    return render_template('post.html', posts=blog_posts)


@app.route('/post.html/<int:post_id>')
def show_one_post(post_id):
    blog_posts = get(url=getenv('POSTS_API')).json()
    requested_post = None
    for post in blog_posts:
        if post['id'] == post_id:
            requested_post = post
            break
    return render_template('post.html', post=requested_post)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
    load_dotenv()
