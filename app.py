from flask import Flask
from flask import render_template,request

app = Flask("__name__") #功能署名
@app.route("/",methods=['Get','POST'])
def index():
    return(render_template('index.html'))

@app.route("/main",methods=['Get','POST'])
def index():
    name = request.form.get("q")
    return(render_template('main.html'))

if __name__ == '__main__': #下划线是系统预留的
    app.run()