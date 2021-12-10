from flask import Flask, render_template

app = Flask(__name__, template_folder="template", static_folder="assets")


@app.route("/")
def my_resume():
    return render_template('index.html')


if __name__ == "__main__":
    app.run('localhost', port=8080, debug=True)
