from flask import Flask, render_template
from flask import url_for
app = Flask(__name__)

name = 'xixi'
movies = [
{'title': 'My Neighbor Totoro', 'year': '1988'},
{'title': 'Dead Poets Society', 'year': '1989'},
{'title': 'A Perfect World', 'year': '1993'},
{'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'},
{'title': 'King of Comedy', 'year': '1999'},
{'title': 'Devils on the Doorstep', 'year': '1999'},
{'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
]

@app.route("/")
def index():
   return render_template('index.html', name=name, movies=movies) 
#需要把图片复制粘贴到同运行文件的目录下  并且"static/1.jpg"/后面有个/ 
#如果是网页图片  要写<img src="http://helloflask.com/totoro.gif">  不写/

