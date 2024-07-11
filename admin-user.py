from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/moder')
def moder():
    return render_template('moder.html')

@app.route('/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

@app.route('/<username>/modify', methods=['GET'])
def modify(username):
    return render_template('modify.html', username=username)


if __name__ == "__main__":
    app.run()