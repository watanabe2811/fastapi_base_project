fake_db = {'johndoe@e.mail': {'password': 'hunter2'}}


class UserModel:
    def get_user(self, email):
        print("try get user ", email)
        return fake_db.get(email)

