from dataclasses import dataclass

@dataclass
class UserDTO:
    id: str
    name: str
    email: str
    org_id: str

    def __init__(self, id: str, name: str, email: str, org_id: str):
        self.id = id
        self.name = name
        self.email = email
        self.org_id = org_id