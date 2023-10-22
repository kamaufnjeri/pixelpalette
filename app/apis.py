from app import app
from app.models import User
from flask import jsonify


@app.route("/api/users")
def all_user():
    all_users = User.query.all()
    users = []
    for user1 in all_users:
        user = {}
        user['username'] = user1.username
        user['first_name'] = user1.first_name
        user['last_name'] = user1.last_name
        user['email_address'] = user1.email_address
        user['category'] = user1.category
        users.append(user)
    return jsonify({"Users": users})