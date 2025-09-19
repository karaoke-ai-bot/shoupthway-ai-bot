from fastapi import APIRouter

router = APIRouter()

# Temporary JSON database
users = []
friends = {}

@router.post("/register")
def register_user(username: str):
    if username in users:
        return {"status": "❌ already exists"}
    users.append(username)
    friends[username] = []
    return {"status": "✅ registered", "username": username}

@router.post("/add-friend")
def add_friend(user: str, friend: str):
    if friend not in users:
        return {"status": "❌ friend not found"}
    if friend in friends[user]:
        return {"status": "⚠ already friends"}
    friends[user].append(friend)
    return {"status": "✅ friend added", "friends": friends[user]}

@router.get("/friends/{username}")
def get_friends(username: str):
    return {"friends": friends.get(username, [])}
