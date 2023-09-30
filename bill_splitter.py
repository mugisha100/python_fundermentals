import random
number_of_friends=int(input("Enter number of friend  including you: \n"))
if number_of_friends <=0:
    print("No one is joining for the party")
else:
    friend_dictionary={}
    print("Enter name of every friend including your name")
    for i in range(number_of_friends):
        name=input()
        # friend_dictionary[name]=0

        friend_dictionary.update({name:0})
    billAmount = float(input("enter bill amount :\n"))
    friend_Bill = float(billAmount /number_of_friends)
    names_of_friend = list(friend_dictionary.keys())

    for name in names_of_friend:
        friend_dictionary.update({name: round(friend_Bill, 2)})

    # print(friend_dictionary)
    # project3
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    response = input()
    if (response.upper() == "YES"):
        random_lucky = random.choice(list(friend_dictionary))
        # friend_dictionary.update({random_lucky: 0})
        print("{} is the lucky one!".format(random_lucky))
        # project4
        for_remaining = billAmount / (number_of_friends - 1)
        for key, value in friend_dictionary.items():
            if key == random_lucky:
                friend_dictionary[random_lucky] = 0
            else:
                friend_dictionary[key] = round(for_remaining, 2)
        print(friend_dictionary)

    else:
        print("No one is going to be lucky")
        print(friend_dictionary)
