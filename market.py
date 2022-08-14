from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

'''
# dynamic route example
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>About page of {username}</h1>'
'''