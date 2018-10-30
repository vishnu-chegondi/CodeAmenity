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

def get_projects_list():
    config = RawConfigParser()
    projects_file = os.path.join(os.path.dirname(__file__),'projects','projects.ini')
    config.read(projects_file)
    projects={}
    for project in config.get('projects','projects').split(','):
        projects[project]={}
        projects[project]['description']=config.get(project,'description')
        projects[project]['tech']=config.get(project,'tech')
        projects[project]['name']=config.get(project,'name')
        projects[project]['gitlink']=config.get(project,'gitlink')
    return projects

if __name__=="__main__":
    print get_projects_list()

