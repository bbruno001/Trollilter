from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests
from app import app 


@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET'])
def register():
    return render_template("register.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route('/log', methods=['POST'])
def return_log():
    data = request.form.to_dict(flat=False)
    print(data)
    return redirect(url_for('explore'))


@app.route("/reg", methods=['POST'])
def return_reg():
    data = request.form.to_dict(flat=False)
    print(data)
    return redirect(url_for('explore'))
