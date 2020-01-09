from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/Datascience')
def Datascience():
    return 'Hello, dear Data Science students'
if __name__=='__main__':
    app.run(debug=True)