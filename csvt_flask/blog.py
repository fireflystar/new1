#coding:utf-8
from flask import Flask, render_template, url_for, request
import os,sqlite3


app = Flask(__name__)

#@app.route('/')
# def index():
# 	username = 'alen'
# 	nav_list = [u'首页',u'经济',u'文化',u'科技',u'娱乐']
# 	blog = {'first':1,'second':2,'third':3,'fourth':4}
# 	return render_template('index.html',
# 		username = username,
# 		nav_list = nav_list,
# 		blog = blog
# 		)


@app.route('/')
def index():
	img = url_for('static', filename = 'images/9.jpg')
	return render_template('index1.html', img=img)
	
     
@app.route('/regist/',methods=['GET','POST'])
def regist():
     if request.method == 'POST':
          #return "regist ok!"
#          print request.form.items()
#          print 'the type of request: ',type(request)
          return "user %s regist ok!" % request.form['username']
     else:
          #request.args['username']
          return render_template("regist.html")

#上传文件       
headimg_path = os.path.join(os.getcwd(),'static')
@app.route('/upload/',methods=['GET','POST'])
def upload():
    if request.method == "POST":
        username = request.form['username']
        headimage = request.files['headimage']
        #print headimage.filename
#        print request.form
#        print request.files
        save_path = os.path.join(headimg_path,headimage.filename)
        headimage.save(save_path)
        return "user is %s, \n file save @   %s" % (username,save_path)
    else:  
        return render_template('upload.html')
        	  
#数据库
@app.route('/db/',methods=['GET','POST'])
def db():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = sqlite3.connect('my.db')
        cursor = conn.cursor()
        sql = "insert into user (username,password) values (?,?)"
        cursor.execute(sql,(username,password))
        conn.commit()
        cursor.close()
        conn.close()
              
        return "%s, %s" % (username,password)
    else:
        return render_template('db.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1',port=5000)