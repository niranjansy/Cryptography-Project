from Cryptography_Utilities.encode import encode
from Cryptography_Utilities.encrypt import encrypt
from Cryptography_Utilities.decode import decode
from Cryptography_Utilities.decrypt import decrypt
from Polynomials.evaluate_polynomial import evaluate_polynomial
from Cryptography_Utilities.decrypt_polynomial import decrypt_polynomial
from colors import bcolors

class Member():

    def __init__(self, id):
        self.id = id
        self.secret_key = None
        self.group_id = None
        self.message_history = []

        print("\nMember {} created.".format(self.id))

    def set_group_id(self, group_id):
        self.group_id = group_id

    def set_secret_key(self, key):
        self.secret_key = key

    def add_message_to_group(self, group, message):

        """
        This is a function that handles the sending of a message by a member to the other members of the group that he is part of.
        The function returns True if message was written successfully, and False otherwise.
        """

        if self.group_id != group.id:
            """
            Inter Group Message
            """
            print("Sending inter-group message from member {} to group {}: {}\n".format(self.id, group.id, message))
            
            key = group.request_intergroup_key(self.id)
            encoded_key = str(bin(key)[2:])
            encoded_message = encode(message)
            encrypted_message = encrypt(encoded_message, encoded_key)
            group.add_intergroup_message(encrypted_message, self.id)

            print("Message has been sent to the group successfully.\n")

        else:
            """
            Intra Group Message
            """
            print(bcolors.BOLD + bcolors.WARNING + "Sending intra-group message from member {} to group {}: {}\n".format(self.id, group.id, message) + bcolors.ENDC)

            group_polynomial = group.get_group_polynomial()
            group_key = evaluate_polynomial(group_polynomial, self.secret_key)
            encoded_message = encode(message)
            encoded_key = str(bin(group_key)[2:])
            encrypted_message = encrypt(encoded_message, encoded_key)
            group.add_message_to_group(encrypted_message)

            print("Message has been added to the group successfully.\n")

        return True

    def read_latest_message_of_group(self, group):

        """
        This is a function for a member to read the latest message that has been sent to his group. 
        Once a message has been added to a group successfully, this function must be called for every member of that group. 
        """

        if self.group_id != group.id:
            print(bcolors.BOLD + bcolors.ERROR + "You are not a member of group ", group.id, "!! \nCannot read messages of the group!!\n" + bcolors.ENDC)
            return False

        if len(group.messages) == 0:
            print(bcolors.BOLD + bcolors.ERROR + "No messages have been sent to the group.\n" + bcolors.ENDC)
            return False

        group_polynomial = group.get_group_polynomial()
        group_key = evaluate_polynomial(group_polynomial, self.secret_key)
        encoded_key = str(bin(group_key)[2:])
        encrypted_message = group.messages[-1]
        decrypted_message = decrypt(encrypted_message, encoded_key)
        decoded_message = decode(decrypted_message)

        print(bcolors.BOLD + bcolors.OKGREEN + "Message read by member {}: {}\n".format(self.id, decoded_message) + bcolors.ENDC)

        self.message_history.append((decoded_message, "Intra-Group"))

        return True

    def read_latest_intergroup_message(self, group):
        """
        This is a function for a member to read the latest message that has been sent to his group from members outside his group. 
        Once a message has been added to a group successfully, this function must be called for every member of that group. 
        """

        if self.group_id != group.id:
            print(bcolors.BOLD + bcolors.ERROR + "You are not a member of group ", group.id, "!! \nCannot read messages of the group!!\n" + bcolors.ENDC)
            return False

        if len(group.intergroup_messages) == 0:
            print(bcolors.BOLD + bcolors.ERROR + "No messages have been sent to the group.\n" + bcolors.ENDC)
            return False

        encrypted_message = group.intergroup_messages[-1][0]
        sender_id = group.intergroup_messages[-1][1]
        group_polynomial = group.get_group_polynomial()
        group_key = evaluate_polynomial(group_polynomial, self.secret_key)
        intergroup_polynomial = decrypt_polynomial(group.intergroup_polynomial, group_key)
        key = evaluate_polynomial(intergroup_polynomial, sender_id)
        encoded_key = str(bin(key)[2:])
        decrypted_message = decrypt(encrypted_message, encoded_key)
        decoded_message = decode(decrypted_message)

        print("Message read by member {}: {}\n".format(self.id, decoded_message))

        self.message_history.append((decoded_message, sender_id))

        return True


    def add_member_to_group(self, member, group):

        """
        This function is for an admin to add a new member to the group. 
        If a group is empty, a member must be added to the group directly and that member will become the admin.
        The subsequent members must be added to the group through the admin. 
        """

        if self.id != group.admin_id:
            print("You are not the admin of the group!! \nCannot add the member to the group!!\n")
            return False

        if not group.add_member(member):
            return False

        return True

    def remove_member_from_group(self, member, group):

        """
        This function is for an admin to remove a member from the group. 
        """

        if self.id != group.admin_id:
            print("You are not the admin of the group!! \nCannot remove the member from the group!!\n")
            return False

        if not group.remove_member(member.id):
            return False

        return True