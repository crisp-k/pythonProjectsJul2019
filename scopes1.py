# scopes1.py
# Local versus Global

# we define a function, called local
def local():
	m = 7
	print (m)

m = 5
print (m)

# we call, or 'execute' the functional local
local()
