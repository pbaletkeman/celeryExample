from flask import Blueprint, render_template

from .tasks import add_user

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def render_form():
    return render_template('form.html')


@main.route('/create_user', methods=['POST'])
def create_user():
    task = add_user.delay()
    return render_template("cancel.html", task=task)


@main.route("/cancel/<task_id>")
def cancel(task_id):
    task = add_user.AsyncResult(task_id)
    task.abort()
    return "CANCELED!"