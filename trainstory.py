start = '''
You wake up one morning and it's 7:30 a.m. and you realize it's a Friday and you have a Girls Who Code trip today.
You quickly get ready and have to decide on what form of transportation you'll take to the Goldman Sachs building.
The options you have are to drive, take the train, or pay $45 for an Uber.
'''


print(start)


print("Type 'drive' to drive or 'train' to take the train or 'uber' to take an uber.")
user_input = input()
#This is what happens if you decide to drive.
if user_input == "drive":
    print("You decide to drive and you have two different potential routes you can take. Type 'FDR' to take the FDR or 'NY-9A' to take the NY-9A.")
    user_input = input()
    if user_input == "FDR":
        print("You decided to take the FDR and got stuck in traffic and arrived to the GS building 30 minutes late and everyone has left. You enter the elevator to go down and find them, but it breaks down. You are heard of again.")
    elif user_input == "NY-9A":
        print("You decided to take the NY-9A and you make it to GS just in time!")
    else:
        print("Invalid option! Try again.")
    # finished the story by writing what happens

#This is what happens if you take the train
elif user_input == "train":
    print("You decided to take the train and have two train routes you can take. Type '4' to take the 4 train or '5' to take the 5 train.")
    user_input = input()
    if user_input == "4":
        print("You are at Grand Central and can transfer to the 6 train or remain on the 4. Type '6' to transfer to the 6 train or 'remain on 4' to remain on the 4 train.")
        user_input = input()
        if user_input == "6":
            print("You made the wrong decision and ended up at the wrong place. You never found your way home and were never heard from again.")
        elif user_input == "remain on 4":
            print("You decided to remain on the 4 and arrived to GS 10 minutes late. The class hasn't left yet, but the teacher is upset because you didn't email.")
        else:
            print("Invalid option! Try again.")
    elif user_input == "5":
        print("You are at 125 St and can walk a couple blocks to transfer to the 2 or remain on the 5 train. Type '2' to transfer to the 2 train or 'remain on 5' to remain on the 5 train.")
        user_input = input()
        if user_input == "2":
            print("You decided to transfer. Unfortunately there was a train accident and a couple flames. You were never heard of again.")
        elif user_input == "remain on 5":
            print("You decided to stay on the 5 and made it alive to Fulton St. and got to GS just in time!")
        else:
            print("Invalid option! Try again.")

#This is what happens if you decide to take an uber.
elif user_input == "uber":
    print("You had to pay $45, but you made it to GS 10 mins early and were able to grab a cup of coffee before heading in.")

    # finished the story writing what happens
else:
    print("Invalid option! Try again.")
