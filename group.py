from Polynomials.generate_polynomial import generate_polynomial
from Polynomials.generate_polynomial import gen_intergroup_polynomial
from Polynomials.evaluate_polynomial import evaluate_polynomial
from Cryptography_Utilities.encrypt_polynomial import encrypt_polynomial
from Cryptography_Utilities.decrypt_polynomial import decrypt_polynomial
# import member

class Group():
    
    def __init__(self, id):

        self.id = id
        self.members = {} # dictionary for stroring (member_id, member object)
        self.secret_keys = [] # list of all secret keys
        self.group_polynomial = None
        self.intergroup_polynomial = None
        self.messages = [] # stores all messages in encrypted form
        self.admin_id = None

        print("\nGroup {} created.".format(self.id))

    def add_member(self, member):
        """
        This function adds a new member to the group. 
        It generates a new group key and a new group polynomial.
        """
        member_id = member.id
        member_key = member.secret_key
        member_group = member.group_id

        if member_group is not None:
            print("\nMember {} already part of Group {}".format(member_id, member_group))
            print("\nCannot add member") 
            return False

        print("\n****** Printing re-keying process *******")

        self.members[member_id] = member
        member.set_group_id(self.id)
        self.secret_keys.append(member_key)

        print("\nMember {} with secret key {} added to Group {}.".format(member_id, member_key, self.id))
        
        if(len(self.secret_keys) == 1):
            print("\nMaking ",member_id," the admin of the group: ",self.id,"\n")
            self.admin_id = member_id

        # Generating new group polynomial and new group key
        self.group_polynomial = generate_polynomial(self.secret_keys)

        # Generating new intergroup polynomial
        group_key = evaluate_polynomial(self.group_polynomial, self.secret_keys[0])
        intergroup_polynomial = gen_intergroup_polynomial(len(self.secret_keys))
        encrpyted_intergroup_polynomial = encrypt_polynomial(intergroup_polynomial, group_key)
        self.intergroup_polynomial = encrpyted_intergroup_polynomial
        print("\nEncrypted Inter Group Polynomial : {}\n".format(self.intergroup_polynomial))

        return True

    def remove_member(self, member_id):
        """
        This function removes a member with given id from the group. 
        It generates a new group key and a new group polynomial.
        """
        
        if member_id not in self.members.keys():
            print("\nMember {} is not part of Group {}".format(member_id, self.id))
            print("\nCannot remove member") 
            return False
        if(member_id == self.admin_id):
            print("Admin of group cannot be removed")
            return False
        
        print("\n****** Printing re-keying process *******")

        member = self.members.pop(member_id)
        member.set_group_id(None)
        self.secret_keys.remove(member.secret_key)
        
        print("\nMember {} with secret key {} removed from Group {}.\n".format(member_id, member.secret_key, self.id))
        
        # Generating new group polynomial and new group key
        self.group_polynomial = generate_polynomial(self.secret_keys)

        # Generating new intergroup polynomial 
        group_key = evaluate_polynomial(self.group_polynomial, self.secret_keys[0])
        intergroup_polynomial = gen_intergroup_polynomial(len(self.secret_keys))
        encrpyted_intergroup_polynomial = encrypt_polynomial(intergroup_polynomial, group_key)
        self.intergroup_polynomial = encrpyted_intergroup_polynomial
        print("\nEncrypted Inter Group Polynomial : {}\n".format(self.intergroup_polynomial))

        return True

    def print_members_list(self):
        
        print("\n****** Printing group members *******")

        member_ids = [i for i in self.members.keys()]
        print("\nThe members in the group are : ", member_ids, "\n")

    def get_group_polynomial(self):
        return self.group_polynomial
    
    def add_message_to_group(self, encrypted_message):
        print("\nAdding encrypted message : ", encrypted_message, " to group\n")
        self.messages.append(encrypted_message)    
