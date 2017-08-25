import turtle
import math

class User:
    def __init__(self, user_name, user_id):
        #recommended attributes
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []

    def addConnection(self, connection_id):
        self.connections.append(connection_id)

    def getUserName(self):
        return self.user_name

    def getConnections(self):
        return self.connections

    def getUserID(self):
        return self.user_id


class Network:
    def __init__(self):
        self.users = []

    def numUsers(self):
        #returns the number of users in the network
        return len(self.users)

    def addUser(self, username):
        # creates a new user, assigns them an ID
        # and adds them to the network
        user_id=len(self.users)
        newUser=User(username, user_id)
        self.users.append(newUser)

    def getUserID(self, username):
        #returns the user id when given the users username
        for person in self.users:
            if (person.getUserName==username):
                return person.getUserID()

    def addConnection(self, user1, user2):
        #This function
        # 1) gets the user ids of user1 and user2
        user_id1=self.getUserID(user1)
        user_id2=self.getUserID(user2)

        user1=self.users[user_id1]
        user2=self.users[user_id2]

        user1.addConnection(user2)
        user2.addConnection(user1)


    #def printUsers(self):
        #BONUS
        #this function goes through the users in the network and prints them

    #def printConnections(self, username):
        #BONUS
        #This function takes in a username, finds the corresponding user, and
        #then prints that users connections

def main():
    facebook=Network()
    print("Welcome to Facebook!")
    username=input("username: ")
    facebook.addUser(username)
    print(facebook.users[0].getUserName())
    print(facebook.users[0].getUserID())
    print("Would you like to add another user?")
    answer=input()
    if (answer=="yes"):
        username=input("username: ")
        facebook.addUser(username)
        print(facebook.users[1].getUserName())
        print(facebook.users[1].getUserID())
    print("Would you liek to make a connection?")
    if (answer=="yes")


main()
