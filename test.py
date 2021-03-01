from group import Group
from member import Member

# Create group
g = Group(id=1)

# Create memebers
m1 = Member(id='Alice', secret_key=23)
m2 = Member(id='Bob', secret_key=37)

# Add members
g.add_member(m1)    # First member to the group has to be added directly, and that person will be the admin
m1.add_member_to_group(m2, g)   # Subsequent new memberships to the group have to be done through the admin of the group 

m1.remove_member_from_group(m1, g) # should not be possible becuse admin cant be removed
m1.remove_member_from_group(m2, g) # should be possible

m1.add_member_to_group(m2, g)

# Get members list
g.print_members_list()


# Writing a message to the group
message = "Attack at midnight"
m1.add_message_to_group(g, message)
m1.read_latest_message_of_group(g)
m2.read_latest_message_of_group(g)


