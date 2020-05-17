from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import requests
from app import app, db
from app.models.forms import LoginForm, RegisterForm
from flask_login import login_user

from app.models.dbconfig import User

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username = login_form.username.data).first()
        if user and user.password == login_form.password.data:
            login_user(user)
            flash("Logged In.")
            return redirect(url_for('explore'))
        else:
            flash("Invalid Login.")
    else:
        print(login_form.errors)
    return render_template("login.html", form=login_form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        instance = User(register_form.username.data, register_form.email.data, register_form.password.data)
        db.session.add(instance)
        db.session.commit()

        return redirect(url_for('login'))
    else:
        print(register_form.errors)
    
    return render_template("register.html", form=register_form)

