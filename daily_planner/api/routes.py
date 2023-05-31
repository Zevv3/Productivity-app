from flask import Blueprint, request, jsonify

from daily_planner.models import db, Task, task_schema, tasks_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/tasks', methods=['POST', 'GET'])
def create_task():
    task_name = request.json['task_name']
    task_content = request.json['task_content']
    days_of_week = request.json['days_of_week']
    repeat_weekly = request.json['repeat_weekly']
    user_token = request.json['user_token']

    task = Task(task_name, task_content, days_of_week, repeat_weekly, user_token)

    db.session.add(task)
    db.session.commit()

    response = task_schema.dump(task)
    return jsonify(response)

@api.route('/tasks/<token>', methods=['GET'])
def get_user_tasks(token):
    tasks = Task.query.filter_by(user_token=token).all()
    response = tasks_schema.dump(tasks)
    return jsonify(response)

@api.route('/tasks/<token>/<id>', methods=['GET'])
def get_one_task(token, id):
    owner = token
    if owner == token:
        task = Task.query.get(id)
        response = task_schema.dump(task)
        return jsonify(response)
    else:
        return jsonify({"error message": "Valid Token Required!"}), 401
    
@api.route('/tasks/<token>,<id>', methods=['POST','PUT'])
def update_task(token, id):
    task = Task.query.get(id)

    task.task_name = request.json['task_name']
    task.task_content = request.josn['task_content']
    task.days_of_week = request.json['days_of_week']
    task.user_token = token

    db.session.commit()
    response = task_schema.dump(task)
    return jsonify(response)

@api.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    
    db.session.delete(task)
    db.session.commit()

    response = task_schema.dump(task)
    return jsonify(response)