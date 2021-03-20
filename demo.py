from group import Group
from member import Member
from absl import app
from absl import flags
import random

FLAGS = flags.FLAGS

groups = {}
members = {}

def print_members_and_groups():
    print("\nMembers : " + str([i for i in members.keys()]))
    print("Groups : " + str([i for i in groups.keys()]))
    if len(groups) > 0:
        print("Members of Groups : ")
    for group in groups.values():
        print("Group {} has members {}".format(group.id, [i for i in group.members.keys()]))

def main(argv):
    print("\n************* Welcome *************\n")
    while True:
        print_members_and_groups()
        print("\nPlease select an action from the following:")
        print("1. Sign Up as a New Member")
        print("2. Log In as an Existing Member")
        print("3. Exit")

        choice = input("\nEnter your choice of action : ")

        if choice == '1':
            """
            Adding a new member.
            """
            print("\n******** Creating Member ********\n")
            mem_id = len(members) + 1
            # key = int(input("Choose a secret key for the member : "))
            key = random.randint(2**FLAGS.l, 2**FLAGS.h)
            m = Member(id=mem_id, secret_key=key)
            members[mem_id] = m
            print("Member created with member id : ", mem_id)
            print("Your secret key is {}. Do not share it with anyone.".format(key))
            print("\n******** Done ********\n")

        elif choice == '2':
            """
            Signing in as existing member by entering member id.
            """
            mem_id = int(input("\nEnter your member ID : "))
            if mem_id not in members.keys():
                print("Invalid member ID!! Please try again.")
                continue

            print("\nLogging in as member {}....".format(mem_id))

            print("\n******** Welcome member {}  ********\n".format(mem_id))

            member = members[mem_id]

            while True:

                print_members_and_groups()

                print("\nPlease select an action from the following: ")
                print("1. Create a new group")
                print("2. Add member to group")
                print("3. Remove member from group")
                print("4. Send message")
                print("5. Read messages")
                print("6. Logout\n")

                option = input("Enter your choice of action : ")

                if option == '1':
                    """
                    Creating a group. 
                    Possible only if the current member is not part of any group.
                    A group will be created with the current member as the admin.  
                    """
                    if member.group_id != None:
                        print("\nYou are already part of a group!!")
                        continue
                    print("\n******** Creating group ********\n")
                    group_id = len(groups) + 1
                    g = Group(id=group_id)
                    g.add_member(member)
                    groups[group_id] = g
                    print("\n******** Done ********\n")
                
                elif option == '2':
                    """
                    Adding a member to a group. This is possible only for a group admin.
                    """
                    g = int(input("Select group : "))
                    m = int(input("Select member : "))
                    if g not in groups.keys() or m not in members.keys():
                        print("Invalid Group or Member ID entered!!")
                        continue
                    group = groups[g]
                    mem = members[m]
                    member.add_member_to_group(mem, group)

                elif option == '3':
                    """
                    Removing a member from a group. This is possible only for a group admin
                    """
                    g = int(input("Select group : "))
                    m = int(input("Select member : "))
                    if g not in groups.keys() or m not in members.keys():
                        print("Invalid Group or Member ID entered!!")
                        continue
                    group = groups[g]
                    mem = members[m]
                    member.remove_member_from_group(mem, group)

                elif option == '4':
                    """
                    Sending a message, intra-group or inter-group
                    """
                    message = input("Enter the message to send : ")
                    g = int(input("Enter the ID of the group to which message is to be sent : "))
                    if g not in groups.keys():
                        print("Invalid Group ID entered!!")
                        continue
                    
                    group = groups[g]
                    member.add_message_to_group(group, message)

                    if g == member.group_id:    # Intra-group message
                        for mem in group.members.values():
                            mem.read_latest_message_of_group(group) 
                            members[mem.id] = mem
                    else:                       # Inter-group message
                        for mem in group.members.values():
                            mem.read_latest_intergroup_message(group)
                            members[mem.id] = mem

                    
                elif option == '5':
                    """
                    Reading messages received on your group
                    """
                    print("Below are the messages received on your group : ")
                    for message in member.message_history:
                        print("\"{}\" - Message received from {}".format(message[0], message[1]))                

                elif option == '6':
                    print("\n******** Logging out the member ********\n")
                    break

                else:
                    print("Invalid choice!! Please try again.")
                


        elif choice == '3':
            print("******** Exiting demo ********\n")
            break

        else:
            print("Invalid choice!! Please try again.")

if __name__ == '__main__':
  app.run(main)