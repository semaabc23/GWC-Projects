class User:
    def __init__(self, username, userid, birthdate, email, connections):
        self.username=username
        self.userid=userid
        self.birthdate=birthdate
        self.email=email
        self.connections=connections

    def getUserName(self):
        return self.username

    def getUserId(self):
        return self.userid

    def getConnections(self):
        return self.connections

    def getBirthdate(self):
        return self.birthdate

    def getEmail(self):
        return self.email

    def from_input(c3ls):
        return cls(
        raw_input('User Name: '),
        int(raw_input('User ID: ')),
        int(raw_input('Birthdate: ')),
        int(raw_input('Email:')),
        int(raw_input('Connections:')),
    )

    user=User.from_input()


class Network:
    def __init__(self):
        self.users=[]
    users={}
    for user in range(10):
        user=user.from_input()
        users[user.userid]=user
    def addUser(self, username):
        self.users.append(username)
        self.userid=numUser


    def addConnection(self, user1, user2):



def main():

    def change_username(username, other_username):
        new_username=other_username
        self.username=new_username

    def change_email(email, other_email):
        new_email=other_email
        self.email=new_email













user_input=input()
# to check duplicates
if user.userid in users:
    raise ValueError('duplicate ID')






















start="Welcome to MySocialNetwork! Do you want to make an account?"
print(start)
if user_input=="Yes":
    print("Great! Type in your name.")



















print "Total User %d" % User.empCount
