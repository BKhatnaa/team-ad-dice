'''
Created on Jan 10, 2017

@author: hanif
'''


from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/khatnaa/santi/crud-application-using-flask-and-mysql-master/source_code/files'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','json'])

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == ' ':
			flash('No selected files')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(url_for('upload_file', filename=filename))
	return render_template('upload_file.html')
@app.route('/')
def index():
    data = db.read(None)
    
    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new post has been added")
        else:
            flash("A new post can not be added")
            
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:
        
        if db.update(session['update'], request.form):
            flash('A post has been updated')
           
        else:
            flash('A post can not be updated')
        
        session.pop('update', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);
    
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:
        
        if db.delete(session['delete']):
            flash('A post has been deleted')
           
        else:
            flash('A post can not be deleted')
        
        session.pop('delete', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

@app.route('/range')
def range():
	return render_template('range.html')

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="0.0.0.0")
