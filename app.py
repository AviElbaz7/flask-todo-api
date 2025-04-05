from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list for demonstration purposes
tasks = [
    {"id": 1, "title": "Study", "done": False},
    {"id": 2, "title": "Go to gym", "done": False}
]

# GET /tasks - Retrieve all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    Return the list of all tasks in JSON format.
    """
    return jsonify(tasks)

# GET /tasks/<id> - Retrieve a task by ID
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """
    Return a single task by its ID.
    If not found, return 404.
    """
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return "Task not found", 404

# POST /tasks - Create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    """
    Create a new task from JSON input.
    Expected format: {"title": "Task name"}
    Returns the created task with new ID and done=False.
    """
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# DELETE /tasks/<id> - Delete a task by ID
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Delete a task by its ID.
    Returns 204 if deleted, or 404 if not found.
    """
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return "Deleted", 204
    return "Task not found", 404

# Run the Flask development server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
