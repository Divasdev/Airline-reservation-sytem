# Passenger class + validation


class Passenger:

    def __init__(self, name, email, phone,):

        self.name = name
        self.email = email
        self.phone = phone


    def validate(self):
        if not self.name.replace(" ","").isalpha():
            return False
        if "@" not in self.email or "." not in self.email:
            return False
        if not self.phone.isdigit():
            return False
        if len(self.phone) < 10 or len(self.phone) > 15:
            return False
        return True
