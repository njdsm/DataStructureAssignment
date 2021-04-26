

class Family:
    def __init__(self):
        self.members = []

    def add_member(self, first_name, last_name, relationship):
        self.members.append({"First Name": first_name, "Last Name": last_name, "Relationship": relationship})
