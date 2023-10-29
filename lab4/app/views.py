from flask import request, render_template, redirect, url_for, make_response, session
from app import app
from datetime import datetime
import os


@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html',
                           os=os.name,
                           user_agent=request.headers.get('User-Agent'),
                           time=datetime.now())


@app.route('/ipz')
def ipz():
    return render_template('ipz.html',
                           os=os.name,
                           user_agent=request.headers.get('User-Agent'),
                           time=datetime.now())


skills = ["Python", "SQL", "Flask", "English", "Teamwork"]


@app.route('/skills')
@app.route('/skills/<int:num>')
def skills_page(num=None):
    if num is not None and num < len(skills):
        return render_template('skill.html',
                               num=num+1,
                               skill=skills[num],
                               os=os.name,
                               user_agent=request.headers.get('User-Agent'),
                               time=datetime.now())
    else:
        return render_template('skills.html',
                               skills=skills,
                               os=os.name,
                               user_agent=request.headers.get('User-Agent'),
                               time=datetime.now())


@app.route('/contact')
def contact():
    return render_template('contact.html',
                           os=os.name,
                           user_agent=request.headers.get('User-Agent'),
                           time=datetime.now())