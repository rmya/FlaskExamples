from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
#from passlib import sha256_crypt

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/articles')
def articles():
  return render_template('articles.html', articles=Articles)

@app.route('/article/<string:id>/')
def article(id):
  return render_template('article.html', id=id)

class RegisterForm(Form):
  name = StringField('Name', [validators.Length(min=1, max=25)])
  username = StringField('Username', [validators.Length(min=4, max=25)])
  email = StringField('Email', [validators.Length(min=6, max=50)])
  password = PasswordField('Password',[
    validators.DataRequired(),
    validators.EqualTo('confirm', message='Password do not match')
  ])
  confirm = PasswordField('Confirm password')

@app.route('/register', methods=['GET','POST'])
def register():
  form = RegisterForm(request.form)
  if request.method == 'POST' and form.validate():
    pass

  return render_template('register.html', form=form)






if __name__ == "__main__":
  app.run(debug=True)   #debug = True ile web sitesinden syntax gibi hataları almamızı sağlıyor ve değişiklikler sırasında serverı yeniden başlatmayı önler.
