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
        if is_valid_email(email):
            dbHandler.insertContact(email, name)
            print(f"Contact added: {email}, {name}")
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
            print("they done goofed")
    else:
        print("add route accessed - GET")
    return render_template('add.html')

def is_valid_email(email):
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.@_-")
    
    for char in email:
        if char not in valid_chars:
            return False
    
    if dbHandler.is_new_email(email):
        print("fuck!")
        return True
    else:
        print("theyu gooded")
        return False


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
