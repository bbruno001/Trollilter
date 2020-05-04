from flask import Flask, render_template, jsonify, request
from app import app 

@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET'])
def register():
    return render_template("register.html")

@app.route("/login/log", methods=['POST'])
def return_log():
    data = request.form.to_dict(flat=False)
    return jsonify(data)

@app.route("/register/reg", methods=['POST'])
def return_reg():
    data = request.form.to_dict(flat=False)
    return jsonify(data)