print "hello max!"

# an if statement:
someImportantValueThatWillChange = 3

x = 1
if x == 1:
    print "wow"

# a for loop:
for x in range(0, 3):
    print "x has this value: %d" % x
    someImportantValueThatWillChange += x

print "done. value of someImportantValueThatWillChange is %d" % someImportantValueThatWillChange
print "For_the_previous *someImportantValueThatWillChange*, I guessed 6, and I was right!"
print "going to sleep now, goodnight!"
for i in range(0, 11):
    print "1"
    print "2"
    print "3"
print "Hello World!"
mystring = "hello"
myfloat = 10.0
myint = 20
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print ("float: %.2f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("integer: %d" % myint)

print "##########################"

# lets ask the user for a number
inputText = raw_input("gimme a number above 100: ")
try:
    num = int(inputText)
except:
    print "that wasn't a number!"
    exit(2)

if num < 101:
    print "you can't count loser!"
    exit(99)

# now we know we have a valid number, so lets do some calculations
for i in range(0, num):
    if i % 10 == 0:
        print i
print num

# end of program
print "bye"


