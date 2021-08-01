from flask import Flask
from flask import url_for
app = Flask(__name__)
@app.route("/")
def hello():
   return '<h1>Welcome to My Watchlist!<h1><img src="static/1.jpg"/>'  
#需要把图片复制粘贴到同运行文件的目录下  并且"static/1.jpg"/后面有个/ 
#如果是网页图片  要写<img src="http://helloflask.com/totoro.gif">  不写/

