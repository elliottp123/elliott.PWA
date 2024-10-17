from flask import Flask, render_template, request, redirect, url_for
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    data = dbHandler.listExtension()
    print("index route accessed")
    return render_template('index.html', content=data)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        dbHandler.insertContact(email, name)
        print(f"Contact added: {email}, {name}")
        return redirect(url_for('index'))
    else:
        print("add route accessed - GET")
        return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
