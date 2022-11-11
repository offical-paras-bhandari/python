class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # self is first parameter and when function is call then know that's object that call it
    def follows(self, user):
        print(user)
        # other user followers goes up by one
        user.followers += 1
        # self following goes up by one
        self.following += 1
        print(self)


user_1 = User("01", "paras")
user_2 = User("02", "Sp")
# user_1 decide to follows user_2
user_1.follows(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)