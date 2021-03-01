class Member():

    def __init__(self, id, secret_key):
        self.id = id
        self.secret_key = secret_key
        self.group_id = None

        print("\nMember {} created.".format(self.id))

    def set_group_id(self, group_id):
        self.group_id = group_id

    def set_secret_key(self, key):
        self.secret_key = key
