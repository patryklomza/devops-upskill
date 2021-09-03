from flask import Blueprint, render_template, request, redirect, url_for

from app.models import Message
from app import db

main = Blueprint('main', __name__)

@main.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template("hello_world.html")
    elif request.method == 'POST':
        new_message = Message(
            user_name=request.form["user_name"],
            email=request.form["email"],
            message=request.form["message"]
        )
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("main.results"))


@main.route('/results', methods=['POST', 'GET'])
def results():
        messages = Message.query.all()
        return render_template("form_results.html", messages=messages)