# Import Flask from the Flask Package
from datetime import datetime
from flask import Flask, render_template, url_for
app = Flask(__name__)

# Creating a variable with a list.
posts = [
    {
        'author': 'Zach Reitan',
        'title': 'Grand Master',
        'content': 'First Blog Post',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Something or other',
        'content': 'Second Blog Post',
        'date_posted': 'April 25, 2018' 
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

@app.route("/testing")
def testing():
    return render_template('testing.html', y=current_time)


if __name__ == '__main__':
    app.run(debug=True)
    