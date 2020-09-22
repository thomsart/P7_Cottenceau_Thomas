from flask import Flask, render_template, jsonify, request

from . import app

from .utilities.tools import put_to_upper_case


app.config.from_object('config')

@app.route('/')
def index():
    return render_template('layouts/default_GrandPy.html')

@app.route('/ajax', methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    reponse = put_to_upper_case(user_text)
    print("test", reponse)
    return jsonify(reponse)


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
