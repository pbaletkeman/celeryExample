from flask import Blueprint, render_template

from .tasks import start_action

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def render_form():
    return render_template('form.html')


@main.route('/start_action', methods=['POST'])
def create_user():
    task = start_action.delay()
    return render_template("cancel.html", task=task)


@main.route("/cancel/<task_id>")
def cancel(task_id):
    task = start_action.AsyncResult(task_id)
    task.abort()
    return "CANCELED!"