from group import Group
from member import Member

# Create group
g = Group(id=1)

# Create memebers
m1 = Member(id='Alice', secret_key=23)
m2 = Member(id='Bob', secret_key=37)

# Add members
g.add_member(m1)
g.add_member(m2)

# Get group key
gk = g.get_group_key()
print("\n****** Group key is : {} ******".format(gk))

# Get members list
g.print_members_list()

# Remove member
g.remove_member(member_id='Bob')


