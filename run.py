from flask import Flask, render_template, request, Markup
from app import deencode

app = Flask(__name__)
app.secret_key = 'abdelali'



# This is The index Page.
@app.route('/')
def index():
    return render_template('index.html')



#This is Encode page.
@app.route('/encode', methods=['GET'])
def index_encode():
    return render_template('encode.html')
@app.route('/encode', methods=['POST'])
def start():
     text = request.form['text']
     hashed = deencode.encode(text)
     html = Markup("<b>Encoded of " + text + " is : " + hashed + " </b>")
     return render_template('encode.html', html= html)


#this is decode page.
@app.route('/decode')
def index_decode():
    return render_template('decode.html')
@app.route('/decode', methods=['POST'])
def startt():
    text = request.form['text']
    return deencode.decode(request.form['text'])
# See app.py lines 12,13,14,15
    #html = Markup("<b>Decoded of " + text + " is : " + decoded + " </b>")
    #return render_template('decode.html', html=html)
@app.errorhandler(404)
def pageNotfound(errodr):
    return render_template('404.html'),404
@app.errorhandler(500)
def server_err(err):
    return render_template('500.html'),500





if __name__ == ('__main__'):

 app.run(host='192.168.1.46', port=8889)
