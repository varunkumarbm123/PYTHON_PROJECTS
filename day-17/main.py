class User:
    def __init__(self,username,age,user_id):
        self.username = username
        self.age = age
        self.user_id = user_id
        self.following = 0
        self.followers = 0

    def follow(self,user):
        user.followers += 1
        self.following+=1

user_1 = User("varun",20,223)
user_2 = User("umesh",21,225)

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
