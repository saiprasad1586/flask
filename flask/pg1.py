from flask import Flask,render_template
 

app = Flask(__name__, template_folder='/templates')

@app.route("/")

@app.route("/home")
def home():
    return render_template('template\home.html')


@app.route("/about")
def about():
    return "<h1>about home page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
