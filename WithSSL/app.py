from flask import Flask, render_template
import socket


app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def display_page():
    hostname = socket.gethostname()    
    ip = socket.gethostbyname(hostname)
    return render_template("index.html", IP=ip, HOST=hostname)

if __name__ == "__main__":
    context = ('localserver.crt', 'localserver.key')
    app.run(host='0.0.0.0', port=5000, ssl_context=context, threaded=True, debug=True)