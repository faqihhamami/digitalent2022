from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>selamat datang peserta DTS di hari ini</h2>"

@app.route('/mahasiswa')
def getmahasiswa():
    return render_template('mahasiswa.html')

@app.route('/jumlah', methods=['GET', 'POST'])
def jumlah():
    if request.method == 'GET':
        return render_template("jumlah/add.html")
    else:
        satu = request.form['satu']
        dua = request.form['dua']

        hasil = int(satu) + int(dua)
        return render_template("jumlah/hasil.html", total=hasil, satu=satu, dua=dua)

@app.route('/celcius', methods=['GET','POST'])
def celcius():
    if request.method == 'GET':
        return render_template("jumlah/inputsuhu.html")
    else:
        inputuser = request.form['celci']
        celtofar = (int(inputuser) * 9/5) + 32
        return render_template("jumlah/konversisuhu.html", celcius=inputuser, farenheit=celtofar)


if __name__ == '__main__':
    app.run(debug=True)