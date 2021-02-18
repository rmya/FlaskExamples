from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')


if __name__ == '__main':
  app.run(debug=True)   #debug = True ile web sitesinden syntax gibi hataları almamızı sağlıyor ve değişiklikler sırasında serverı yeniden başlatmayı önler.
