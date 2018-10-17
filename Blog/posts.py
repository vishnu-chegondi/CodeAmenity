from ConfigParser import RawConfigParser
import os

def get_articles_list(articles_dir):
    articles = os.listdir(articles_dir)
    return articles

def get_posts_list():
    posts={}
    present_dir = os.path.dirname(__file__)
    articles_dir = os.path.join(present_dir,'articles')
    articles = get_articles_list(articles_dir)
    for article in articles:
        article_path = os.path.join(articles_dir,article)
        posts_temp = os.listdir(article_path)
        posts_temp = [os.path.splitext(i)[0] for i in posts_temp]
        posts[article]=posts_temp
    return posts
