#!-*- coding: utf-8 -*-
from flask import render_template

from app import app
from .forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"nickname": "Alex"}
    title = "Alex's Home Page"
    return render_template("home.html", title=title, user=user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                            title = 'Sign In',
                            form = form)
