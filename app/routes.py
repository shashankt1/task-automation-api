from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import db, Task  # ✅ FIXED: Correct import path
from app.tasks import execute_task

routes = Blueprint('routes', __name__)

@routes.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    
    # Create new task
    new_task = Task(name=data['name'])
    db.session.add(new_task)
    db.session.commit()
    
    # Execute task asynchronously
    execute_task.apply_async(args=[new_task.id])

    return jsonify({"message": "Task scheduled", "task_id": new_task.id})

@routes.route('/tasks/<task_id>', methods=['GET'])
@jwt_required()
def get_task_status(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    return jsonify({"task_id": task.id, "status": task.status})