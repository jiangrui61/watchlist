from flask import Flask
from flask import url_for
app = Flask(__name__)
@app.route("/")
def hello():
   return '<h1>Welcome to My Watchlist!<h1><img src="static/1.jpg"/>'  
#��Ҫ��ͼƬ����ճ����ͬ�����ļ���Ŀ¼��  ����"static/1.jpg"/�����и�/ 
#�������ҳͼƬ  Ҫд<img src="http://helloflask.com/totoro.gif">  ��д/

