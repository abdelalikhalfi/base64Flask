import base64
from flask import Flask, render_template, Markup


class deencode(object):
    @staticmethod
    def encode(a):
        return base64.b64encode(a)
    @staticmethod
    def decode(b):
        try:
          base64.b64decode(b)
          html = Markup("<b>Decoded code  : " + base64.b64decode(b) + " </b>")
          return render_template('encode.html', html=html)
        except:
            return render_template('encode.html', html="Invalid Code")





