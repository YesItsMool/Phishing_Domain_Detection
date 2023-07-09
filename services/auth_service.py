# services/auth_service.py
from typing import List
from models.user import User

class UserManager:
    def __init__(self):
        self.users: List[User] = []

    def register_user(self, user: User):
        if any(u for u in self.users if u.username == user.username or u.email == user.email):
            return False
        self.users.append(user)
        return True

    def get_user(self, username: str):
        return next((u for u in self.users if u.username == username), None)
