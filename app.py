import io
import os
import json

from flask import Flask, render_template, request
app = Flask(__name__)

common = {
    'first_name': 'Raymond',
    'last_name': 'Mills',
    'alias': ''
}

@app.route("/")
def index():
    return render_template("home.html", common=common)

@app.route('/projects')
def projects():
    data = get_static_json("static/projects/projects.json")['projects']
    data.sort(key=order_projects, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower() for project_tag in project['tags']]]
    return render_template('projects.html', common=common, projects=data, tag=tag)

def order_projects(projects):
    try: 
        return int(projects['weight'])
    except KeyError:
        return 0

@app.route('/projects/<title>')
def project(title):
    projects = get_static_json("static/projects/projects.json")['projects']
    
    in_project = next((p for p in projects if p['link'] == title), None)

    # ERROR HANDLER
    
    # load html if the json file doesn't contain a description
    if 'description' not in selected:
        
        selected['description'] = io.open(get_static_file(
            'static/%s/%s/%s.html' % (path, selected['link'], selected['link'])), "r", encoding="utf-8").read()
    return render_template('project.html', common=common, project=selected)




