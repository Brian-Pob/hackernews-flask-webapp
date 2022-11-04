import sys
from flask import render_template, redirect, url_for, session
from app import app, db
from app.models import User, Post, admins
import json
import requests
from sqlalchemy import select, or_

from flask_caching import Cache
import httpx
import asyncio

cache = Cache(app)

base_url = 'https://hacker-news.firebaseio.com/v0/'

import datetime

@app.route("/")
def index():
    #to_return = "<img src='/static/images/stars.jpg' alt='no image found'>"
    #image_url = url_for('memes', filename='spongebob-leak.gif')
    image_url = '/memes/spongebob-leak.gif'
    to_return = "<img src='%s' alt='no image found!!'>" % (image_url)
    to_return += "<a href='/login'>Login</a><a href='/home'>Home</a>"
    session_user = dict(session).get('user', None)
    if (session_user):
        to_return = to_return + "<p>User {} is logged in</p>".format(session_user["userinfo"]["name"])
    return '<p>hello. This is a Python Flask app running with Gunicorn and Nginx! 🐍+🧪+🦄+🚙 = ⚡️💪🔥</p>' + to_return + image_url

@app.route("/home")
def home():
    users = []
    uid = -1
    try:
        uinfo = dict(session).get('user', None)
        uinfo = dict(uinfo).get('userinfo', None)
        stmt = select(User.id).where(User.email == uinfo['email'])
        try:
            users = db.session.execute(stmt).first() 
            print(type(users))
            print((users._asdict()))
            uid = users._asdict()['id']
            parsed = json.dumps((session), indent=4) 
        except Exception as e:
            print("Error in db access")
    except Exception as e:
        print(e)
        print("Error in user session")
     
    posts = asyncio.run(getposts())
    sys.stdout.flush()
    return render_template("home.html", session=dict(session).get('user', None), users=users, posts=posts, isadmin=isadmin(uid)) 

async def getposts():
    async with httpx.AsyncClient() as s:
        top = (await s.get(base_url + 'topstories.json')).json()
        tasks = [s.get(base_url+'/item/'+str(article)+'.json') for article in top]
        posts = await asyncio.gather(*tasks)
        posts = [story.json() for story in posts]
        return posts

def isadmin(user_id):
    try:
        stmt = select(admins).where(admins.c.user_id == user_id)
        admin = db.session.execute(stmt).first()
        print(admin)
        sys.stdout.flush()
        return admin != None
    except Exception as e:
        print(e)
        return False
