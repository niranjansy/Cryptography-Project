from group import Group
from member import Member

# Create group
g = Group(id=1)

# Create memebers
admin = Member(id=0, secret_key=23)
member1 = Member(id=1, secret_key=37)
member2 = Member(id=2, secret_key=71)
member3 = Member(id=3, secret_key=79)

# Add members
# First member to the group has to be added directly, and that person will be the admin
g.add_member(admin)

# Subsequent new memberships to the group have to be done through the admin of the group 
admin.add_member_to_group(member1, g)  
admin.add_member_to_group(member2, g)  

# Not possible as other members of the group, apart from the admin 
# cannot add new members to the group
member1.add_member_to_group(member3, g)

# Admin can remove members from the group
admin.remove_member_from_group(member2, g)

# Not possible as other members of the group, apart from the admin 
# cannot remove any member of the group 
member1.remove_member_from_group(admin, g) 

# Admin of the group cannot be removed
admin.remove_member_from_group(admin, g) 

# Print all the members in the group
g.print_members_list()

# Writing an intra-group message
message = "Attack at midnight"

# A member can send a message to the group
member1.add_message_to_group(g, message)

# Any other member of the group can read the message
admin.read_latest_message_of_group(g)

# As member3 is not part of the group, message cant be read by member3
member3.read_latest_message_of_group(g)

# Writing inter-group message by member3 to group g
message = "Don't attack"
member3.add_message_to_group(g, message)
member1.read_latest_intergroup_message(g)


