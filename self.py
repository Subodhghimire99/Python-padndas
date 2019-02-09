class test:
	def __init__(self,name,address,gmail):
		self.name = name
		self.address = address
		self.gmail = gmail
	def display(self):
		print("Username :: {0} \nGmail id :: {1}\nAddress is : {2}".format(self.name, self.gmail, self.address))
# user1=test("Subodh","Barangdi","subodhghimire99@gmail.com")
# all_user_list=[]
# decide=input("Do you want to insert new user?")
new_user=[]
def add_user():
	username=input("Enter Username :-  ")
	gmail=input("Enter yout gmail :-  ")
	address=input("Enter the address :-  ")
	new_user.append(username)
	new_user.append(gmail)
	new_user.append(address)
add_user()
print(new_user)
