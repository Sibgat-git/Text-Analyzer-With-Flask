from flask import Flask , render_template, url_for, request,redirect
import os

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    techs = ['HTML','CSS','Flask','Python']
    name= '30 Days of Python Programming'
    return render_template('home.html', techs=techs,name=name,title='Okaeri')

@app.route('/about')
def about():
    name = '30 Days of Python Programming'
    return render_template('about.html',name=name,title='About us')

@app.route('/post')
def post():
    name= 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html',title=name,name=name)
    if request.method == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

    return render_template('post.html',name=name,title=name)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000)) #makes app cloud ready
    app.run(debug=True, host='0.0.0.0', port=port)