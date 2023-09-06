from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class UserDTO:
    name: str
    email: str
    password: str
    id: int = None

    def __post_init__(self):
        self.password = generate_password_hash(self.password, method='pbkdf2', salt_length=8)
