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

g.remove_member(m1.id) # should not be possible becuse admin cant be removed
g.remove_member(m2.id) # should be possible


# Get members list
g.print_members_list()

# Remove member
g.remove_member(member_id='Bob') # this should show not possible

