from group import Group
from member import Member

groups = {}
members = {}

print("\n******** Welcome ********\n")
while True:
    print("Groups : " + str([i for i in groups.keys()]))
    print("Members : " + str([i for i in members.keys()]))

    print("Please select an action from the following\n")
    print("1. Create new Group")
    print("2. Create new Member")
    print("3. Add member to group")
    print("4. Remove member from group")
    print("5. Send message")
    print("6. Read message")
    print("7. Quit the demo\n")
    
    choice = input("Enter your choice of action : ")

    if choice=='1':
        print("******** Creating group ********\n")
        group_id = len(groups)+1
        g = Group(id=group_id)
        groups[group_id]=g
        print("\n******** Done ********\n")
    
    elif choice=='2':
        print("******** Creating member ********\n")
        mem_id = len(members)+1
        key = int(input("Choose a secret key for the member : "))
        m = Member(id=mem_id, secret_key=key)
        members[mem_id]=m
        print("\n******** Done ********\n")

    elif choice=='3':
        print("******** Adding member to group ********\n")
        g = int(input("Select group : "))
        m = int(input("Select member : "))
        group = groups[g]
        mem = members[m]
        if group.admin_id == None:
            print("Adding first member to group")
            group.add_member(mem)
        else:
            admin_id = group.admin_id
            admin = members[admin_id]
            admin.add_member_to_group(mem, group)
        print("\n******** Done ********\n")

    elif choice=='4':
        print("******** Removing member from group ********\n")
        g = int(input("Select group : "))
        m = int(input("Select member : "))
        group = groups[g]
        mem = members[g]
        if group.admin_id == None:
            print("Group is empty")
        else:
            admin_id = group.admin_id
            admin = members[admin_id]
            admin.remove_member_to_group(mem, group)
        print("\n******** Done ********\n")

    elif choice=='7':
        print("******** Exiting demo ********\n")
        break





    