from ConfigParser import RawConfigParser
import os
import boto3
import tempfile

def get_articles_list():
    client = boto3.client('s3')
    response = client.list_objects(
        Bucket='codeamenity',
        Prefix='articles/',
    )
    keys = [str(i['Key']) for i in response['Contents']]
    articles = {}
    for key in keys:
        tmp = key.split('/')
        if tmp[1] not in articles.keys():
            articles[tmp[1]] = []
        articles[tmp[1]].append(tmp[2].split('.')[0])
    return articles

def get_projects_list():
    config = RawConfigParser()
    key = 'projects/projects.ini'
    client = boto3.client('s3')
    response = client.get_object(Bucket='codeamenity',Key=key)
    content = response["Body"].read()
    filename = tempfile.NamedTemporaryFile().name
    with open(filename,"w+") as fp:
        fp.write(content)
    config.read(filename)
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

