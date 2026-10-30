
from fastapi import FastAPI

app = FastAPI(title="FastAPI Docker App")


# Home route
@app.get("/")
def home():
    return {"message": "Hello from FastAPI Docker Deployment!"}


# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}


# Get all users
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Nauman"},
        {"id": 2, "name": "Ali"},
        {"id": 3, "name": "Ahmed"}
    ]


# Get user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Nauman"}


# Create a user
@app.post("/users")
def create_user(user: dict):
    return {
        "message": "User created successfully",
        "user": user
    }


# Update a user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    return {
        "message": "User updated successfully",
        "user_id": user_id,
        "updated_data": user
    }


# Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted successfully",
        "user_id": user_id
    }


# About API
@app.get("/about")
def about():
    return {
        "application": "FastAPI Docker App",
        "language": "Python",
        "framework": "FastAPI"
    }
