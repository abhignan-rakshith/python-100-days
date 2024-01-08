# Learning to create classes in PascalCase
# Learnt pass keyword
# Learnt __init__ method to initialize attributes using 'parameters'
# Now, while creating new 'User' objects, we 'need' to specify the required parameters
# Learnt Defaulting attributes

class User:
    def __init__(self, user_id, username):
        print("new user being added")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following =0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1 = User("001", "abhignan-rakshith")
user_2 = User("002", "vihitha-nayana")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)