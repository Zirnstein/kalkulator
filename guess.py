from random import randint

secret = randint(0, 20)
guess = 0


while guess != secret:

    guess = int(raw_input("Guess the secret number (between 1 and 20):  "))

    if guess == secret:
        print "You guessed it- congratulations! It's number {0} : ))))".format(secret)
    elif guess > secret:
        print "Your  guess is not correct...try something smaller"
    elif guess < secret:
        print "Your guess is not correct...try something bigger"
    else:
        print "Sorry, your guess is not correct...Secret number is not {guess_val}.".format(guess_val=guess)



# for i in range(5):   #gre od 0 do 4
#     guess = int(raw_input("Guess the secret number (between 1 and 20):  "))
#
#     if guess == secret:
#         print "You guessed it- congratulations! It's number {0} :".format(secret)
#         break
#     else:
#         print "Sorry, your guess is not correct...Secret number is not {guess_val}.".format(guess_val=guess)
#
#
# print secret
