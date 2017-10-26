x = int(raw_input(" Vpisi stevilo: "))


for i in range(0, x):

    if (i % 3 == 0):
        print "{0} Fizz".format(i)
    elif (i % 5 == 0):
        print "{0} Buzz".format(i)
    elif (i % 3 == 0 and i % 5 == 0):
        print "{0} FizzBuzz".format(i)

    else:
        # print "Tvoje stevilo je {param}.".format(param=i)
        print "Tvoje stevilo je {0}".format(i)



