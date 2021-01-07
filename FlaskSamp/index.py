from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route("/")
def anasayfa():
  return "Merhaba"

@app.route("/iletisim")
def iletisim():
  return "Burası iletişim sayfası"

@app.route("/hakkimizda")
def hakkimizda():
  return "Burada da kendimizi tanıtacağız"
"""

""" ***Dinamik URL
@app.route('/yazar/<string:id>')
def yazar(id):
  return "Kitap ID si:" + id
"""

"""
#Hakkimizda Sayfasi
@app.route('/hakkimizda')
def hakkimizda():       #render_template fonksiyonu ile route'a ilgili sayfaya gidildiğinde hangi dosyanın yükleneceğini gösterebiliyoruz.
  return render_template("hakkimizda.html")
"""

#Yüklenecek sayfaya değişken göndermek için: Örneğin ben title isimli bir değişken göndererek HTML sayfasının içinde title meta etiketini otomatik oluşturmak ve sayfaya id değeri vermek için ayriyeten bir değişken daha göndermek istiyorum. Bunun için de fonksiyonumuzda direkt değişkeni belirleyerek gönderebilirsiniz
#Hakkimizda Sayfasi
@app.route('/hakkimizda')
def hakkimizda():
  id = 3
  return render_template("hakkimizda.html",sayfabasligi="Hakkımızda Sayfası", sayfaid = id)

#Hizmetler Sayfası
@app.route('/hizmetler')
def hizmetler():
  return render_template("hizmetler.html")

#Bebek Bakıcılığı Sayfası
@app.route('/bebek-bakiciligi')
def bebekbakiciligi():
  return render_template("bebek-bakiciligi.html")

if __name__ == "__main__":
    app.run(debug=True)      #Flaskın ana proğram olarak çalıştığından emin oluyoruz

#Sunucumuz default adres olan 127.0.0.1:5000 adresi üzerinden çalışır.