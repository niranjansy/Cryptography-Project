from group import Group
from member import Member
from absl import app
from absl import flags
from colors import bcolors
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
        print(bcolors.BOLD + bcolors.WARNING + "\nPlease select an action from the following:" + bcolors.ENDC)
        print(bcolors.BOLD + bcolors.WARNING + "1. Sign Up as a New Member" + bcolors.ENDC)
        print(bcolors.BOLD + bcolors.WARNING + "2. Log In as an Existing Member" + bcolors.ENDC)
        print(bcolors.BOLD + bcolors.WARNING + "3. Exit" + bcolors.ENDC)

        choice = input("\nEnter your choice of action : ")

        if choice == '1':
            """
            Creating a new member.
            """
            print("\n******** Creating Member ********\n")
            mem_id = len(members) + 1
            # key = int(input("Choose a secret key for the member : "))
            # key = random.randint(2**FLAGS.l, 2**FLAGS.h)
            m = Member(id=mem_id)
            members[mem_id] = m
            print("Member created with member id : ", mem_id)
            # print(bcolors.BOLD + bcolors.OKBLUE + "Your secret key is {}. Do not share it with anyone.".format(key) + bcolors.ENDC)
            print("\n******** Done ********\n")

        elif choice == '2':
            """
            Signing in as existing member by entering member id.
            """
            mem_id = int(input(bcolors.BOLD + bcolors.WARNING + "\nEnter your member ID : "+bcolors.ENDC))
            if mem_id not in members.keys():
                print(bcolors.BOLD + bcolors.ERROR + "Invalid member ID!! Please try again."+bcolors.ENDC)
                continue

            print(bcolors.BOLD + bcolors.OKGREEN + "\nLogging in as member {}....".format(mem_id)+bcolors.ENDC)

            print("\n******** Welcome member {}  ********\n".format(mem_id))

            member = members[mem_id]

            while True:

                print_members_and_groups()

                print(bcolors.BOLD + bcolors.WARNING + "\nPlease select an action from the following: "+bcolors.ENDC)
                print(bcolors.BOLD + bcolors.WARNING + "1. Create a new group"+bcolors.ENDC)
                print(bcolors.BOLD + bcolors.WARNING + "2. Add member to group"+bcolors.ENDC)
                print(bcolors.BOLD + bcolors.WARNING + "3. Remove member from group"+bcolors.ENDC)
                print(bcolors.BOLD + bcolors.WARNING + "4. Send message"+bcolors.ENDC)
                print(bcolors.BOLD + bcolors.WARNING + "5. Read messages"+bcolors.ENDC)
                print(bcolors.BOLD + bcolors.WARNING + "6. Logout\n"+bcolors.ENDC)

                option = input(bcolors.BOLD + bcolors.WARNING + "Enter your choice of action : "+bcolors.ENDC)

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
                    if member.group_id == None:
                        print("\nYou are not a member of any group!!")
                        continue

                    m = int(input("Select member : "))
                    if m not in members.keys():
                        print("Invalid Member ID entered!!")
                        continue
                    g = member.group_id
                    group = groups[g]
                    mem = members[m]
                    member.add_member_to_group(mem, group)

                elif option == '3':
                    """
                    Removing a member from a group. This is possible only for a group admin
                    """
                    if member.group_id == None:
                        print("\nYou are not a member of any group!!")
                        continue
                    m = int(input("Select member : "))
                    if m not in members.keys():
                        print("Invalid Member ID entered!!")
                        continue
                    g = member.group_id
                    group = groups[g]
                    mem = members[m]
                    member.remove_member_from_group(mem, group)

                elif option == '4':
                    """
                    Sending a message, intra-group or inter-group
                    """
                    message = input(bcolors.BOLD + bcolors.WARNING + "Enter the message to send : " + bcolors.ENDC)
                    g = int(input(bcolors.BOLD + bcolors.WARNING + "Enter the ID of the group to which message is to be sent : " + bcolors.ENDC))
                    if g not in groups.keys():
                        print(bcolors.BOLD + bcolors.ERROR + "Invalid Group ID entered!!" + bcolors.ENDC)
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
                    print(bcolors.BOLD + bcolors.WARNING + "Below are the messages received on your group : "+bcolors.ENDC)
                    for message in member.message_history:
                        print("\"{}\" - Message received from {}".format(message[0], message[1]))                

                elif option == '6':
                    print(bcolors.BOLD + bcolors.OKGREEN + "\n******** Logging out the member ********\n"+bcolors.ENDC)
                    break

                else:
                    print(bcolors.BOLD + bcolors.ERROR + "Invalid choice!! Please try again."+bcolors.ENDC)
                


        elif choice == '3':
            print("******** Exiting demo ********\n")
            break

        else:
            print(bcolors.BOLD + bcolors.ERROR + "Invalid choice!! Please try again." + bcolors.ENDC)

if __name__ == '__main__':
  app.run(main)