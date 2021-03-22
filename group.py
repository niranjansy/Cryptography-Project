from Polynomials.generate_polynomial import generate_polynomial
from Polynomials.generate_polynomial import gen_intergroup_polynomial
from Polynomials.evaluate_polynomial import evaluate_polynomial
from Cryptography_Utilities.encrypt_polynomial import encrypt_polynomial
from Cryptography_Utilities.decrypt_polynomial import decrypt_polynomial
from colors import bcolors
# import member

from absl import app
from absl import flags
import random

FLAGS = flags.FLAGS

class Group():
    
    def __init__(self, id):

        self.id = id
        self.members = {} # dictionary for storing (member_id, member object)
        self.secret_keys = [] # list of all secret keys
        self.group_polynomial = None
        self.intergroup_polynomial = None
        self.messages = [] # stores all intra-group messages in encrypted form
        self.intergroup_messages = []   # stores encrypted messages from members ouside the group, in the form of pairs - (encrypted_message, sender_id)
        self.admin_id = None

        print("\nGroup {} created.".format(self.id))

    def add_member(self, member):
        """
        This function adds a new member to the group. 
        It generates a new group key and a new group polynomial.
        """
        member_id = member.id
        member_group = member.group_id

        if member_group is not None:
            print("\nMember {} already part of Group {}".format(member_id, member_group))
            print("\nCannot add member") 
            return False

        print("\n****** Printing re-keying process *******")

        member_key = random.randint(2**FLAGS.l, 2**FLAGS.h)
        member.set_group_id(self.id)
        member.set_secret_key(member_key)
        self.members[member_id] = member
        self.secret_keys.append(member_key)

        print(bcolors.BOLD + bcolors.OKGREEN + "\nMember {} with secret key {} added to Group {}.".format(member_id, member_key, self.id) + bcolors.ENDC)
        
        if(len(self.secret_keys) == 1):
            print(bcolors.BOLD + bcolors.OKGREEN + "\nMaking ",member_id," the admin of the group: ",self.id,"\n" + bcolors.ENDC)
            self.admin_id = member_id

        # Generating new group polynomial and new group key
        self.group_polynomial = generate_polynomial(self.secret_keys)

        # Generating new intergroup polynomial
        group_key = evaluate_polynomial(self.group_polynomial, self.secret_keys[0])
        intergroup_polynomial = gen_intergroup_polynomial(len(self.secret_keys))
        encrpyted_intergroup_polynomial = encrypt_polynomial(intergroup_polynomial, group_key)
        self.intergroup_polynomial = encrpyted_intergroup_polynomial
        print(bcolors.BOLD + bcolors.OKGREEN + "\nEncrypted Inter Group Polynomial : " + bcolors.ENDC + self.intergroup_polynomial)

        return True

    def remove_member(self, member_id):
        """
        This function removes a member with given id from the group. 
        It generates a new group key and a new group polynomial.
        """
        
        if member_id not in self.members.keys():
            print(bcolors.BOLD + bcolors.ERROR +"\nMember {} is not part of Group {}".format(member_id, self.id) + bcolors.ENDC)
            print(bcolors.BOLD + bcolors.ERROR +"\nCannot remove member" + bcolors.ENDC) 
            return False
        if(member_id == self.admin_id):
            print(bcolors.BOLD + bcolors.ERROR + "Admin of group cannot be removed" + bcolors.ENDC)
            return False
        
        print("\n****** Printing re-keying process *******")

        member = self.members.pop(member_id)
        member.set_group_id(None)
        self.secret_keys.remove(member.secret_key)
        
        print(bcolors.BOLD + bcolors.OKGREEN +"\nMember {} with secret key {} removed from Group {}.\n".format(member_id, member.secret_key, self.id) + bcolors.ENDC)
        
        # Generating new group polynomial and new group key
        self.group_polynomial = generate_polynomial(self.secret_keys)

        # Generating new intergroup polynomial 
        group_key = evaluate_polynomial(self.group_polynomial, self.secret_keys[0])
        intergroup_polynomial = gen_intergroup_polynomial(len(self.secret_keys))
        encrpyted_intergroup_polynomial = encrypt_polynomial(intergroup_polynomial, group_key)
        self.intergroup_polynomial = encrpyted_intergroup_polynomial
        print(bcolors.BOLD + bcolors.OKGREEN +"\nEncrypted Inter Group Polynomial : {}\n".format(self.intergroup_polynomial) + bcolors.ENDC)

        return True

    def print_members_list(self):
        
        print("\n****** Printing group members *******")

        member_ids = [i for i in self.members.keys()]
        print("\nThe members in the group are : ", member_ids, "\n")

    def get_group_polynomial(self):
        return self.group_polynomial
    
    def add_message_to_group(self, encrypted_message):
        print(bcolors.BOLD + bcolors.OKGREEN +"\nAdding encrypted message : " +  bcolors.ENDC + encrypted_message + " to group\n")
        self.messages.append(encrypted_message)    

    def request_intergroup_key(self, member_id):
        """
        This function returns an inter-group key, 
        when a member outside the group requests for the key to send a message to the group.
        """

        group_key = evaluate_polynomial(self.group_polynomial, self.secret_keys[0])
        decrypted_polynomial = decrypt_polynomial(self.intergroup_polynomial, group_key)
        intergroup_key = evaluate_polynomial(decrypted_polynomial, member_id)
        print(bcolors.BOLD + bcolors.OKGREEN + "Evaluated inter group key : " + bcolors.ENDC + str(intergroup_key))

        return intergroup_key

    def add_intergroup_message(self, encrypted_message, member_id):
        print(bcolors.BOLD + bcolors.OKGREEN + "\nAdding encrypted message {} from member {} to the group\n".format(encrypted_message, member_id) + bcolors.ENDC)
        self.intergroup_messages.append((encrypted_message, member_id))

