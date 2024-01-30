from flask import Flask 

# creating an instance
app= Flask(__name__)

@app.route('/home')
def home():
    return'<h2> Flask by Taaka Esther</h2>'