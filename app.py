from flask import Flask
app = Flask(__name__)

@app.route('/test-spring')
def home():
   return 'Chrome - Spring - Flask success!'

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)