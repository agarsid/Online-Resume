from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/about/')
# def about():
#     return render_template("about.html")

# @app.route('/experience/')
# def exp():
#     return render_template("experience.html")

# @app.route('/education/')
# def edu():
#     return render_template("education.html")

# @app.route('/projects/')
# def proj():
#     return render_template("projects.html")

# @app.route('/skills/')
# def skills():
#     return render_template("skills.html")

# @app.route('/contact/')
# def contact():
#     return render_template("contact.html")


if(__name__=="__main__"):
    app.run(debug=True)