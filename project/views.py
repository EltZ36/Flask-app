from project import app 
from flask import render_template, url_for

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html',name = name)

@app.route('/list')
def listItems():
  name = ["Throckmorton", "Ethan", "Alvin"]
  return render_template('names.html', name = name)