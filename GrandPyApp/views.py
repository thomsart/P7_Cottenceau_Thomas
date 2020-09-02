from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('pages/answers_GrandPy.html')


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
