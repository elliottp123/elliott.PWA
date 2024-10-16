from flask import Flask, render_template, request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])

def index():
   data = dbHandler.listExtension()
   print("inx route accessed")
   return render_template('index.html', content=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
   print("Add route accessed")
   return render_template('add.html')  # or just 'add.html' if it's in the main templates folder

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)