import sys
import os
import boto3

sys.path.append(os.path.dirname(__file__))
from flask import Flask,render_template,Markup
from posts import get_articles_list, get_projects_list
from markdown import markdown

app = Flask(__name__)


@app.route('/')
def index():
    '''
    This returns the Index page
    '''
    articles = get_articles_list()
    projects = get_projects_list()
    # content = """#### Welcome to CodeSlips
    # """
    # content = Markup(markdown(content))
    return render_template('index.html',**locals())

@app.route('/post/<article>/<post>')
def post_data(article,post):
    '''
    This returns the content of mrkdown
    '''
    articles = get_articles_list()
    client = boto3.client('s3')
    key = "articles/"+article+"/"+post+".md"
    response = client.get_object(Bucket='codeamenity',Key=key)
    content = Markup(markdown(response["Body"].read()))
    return render_template('index.html',**locals())

@app.route('/author')
def author():
    '''
    This returns the author information
    '''
    return render_template('author.html')


if __name__=="__main__":
    app.run()