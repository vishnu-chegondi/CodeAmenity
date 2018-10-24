import sys
import os

sys.path.append(os.path.dirname(__file__))
from flask import Flask,render_template,Markup
from posts import get_posts_list
from markdown import markdown

app = Flask(__name__)


@app.route('/')
def index():
    '''
    This returns the Index page
    '''
    articles = get_posts_list()
    # content = """#### Welcome to CodeSlips
    # """
    # content = Markup(markdown(content))
    return render_template('index.html',**locals())

@app.route('/post/<article>/<post>')
def post_data(article,post):
    '''
    This returns the content of mrkdown
    '''
    articles = get_posts_list()
    file = os.path.join(os.path.dirname(__file__),"articles",article,post+'.md')
    fobj = open(file).read()
    content = Markup(markdown(fobj))
    return render_template('index.html',**locals())

@app.route('/author')
def author():
    '''
    This returns the author information
    '''
    return render_template('author.html')


if __name__=="__main__":
    app.run()