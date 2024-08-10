from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)


datal = ["I", "G", "S"]

@app.route("/")
def home():
    return render_template("home.html", biodata="Konten Biodata Anda")

@app.route('/biodata')
def biodata():
    if 'namas' in request.args.keys() and 'umurs' in request.args.keys():
        nama = request.args['namas']
        umur = request.args['umurs']
        kelas = request.args.get('kelass')
        return render_template("biodata.html", datal = datal)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)