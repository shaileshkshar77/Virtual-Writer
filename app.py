from flask import Flask,render_template,request, redirect, url_for
from main import main

app = Flask(__name__)
#commitmessage
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/AR')
def AR():
    text1 = main()
    return render_template("AR.html",text =text1)

if(__name__=="__main__"):
    app.run(debug=True)