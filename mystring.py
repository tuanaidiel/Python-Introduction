message = "Hello world"
message = 'Hello world'

# upper method
print (message.upper())
print (message)     #not converted permanently / not inline
                    #inline means do the changes and assign the changed value
                    #to the same variable

uppermessage = message.upper()
print (uppermessage)

print (message.lower())
print (message.capitalize())

print ("----------------------------------------------------------------")

print ("JCG" + str (8949))

#2nd method
carplate = "JCG"
number = 8949
carplatenumber = f"{carplate}{number}"
print (carplatenumber)

print ("----------------------------------------------------------------")

filepath = "c: \newfolder\table\report.txt"  #add '\' to solve this problem
print (filepath)
filepath = "c: \\newfolder\\table\\report.txt"
print (filepath)
filepath = r"c: \newfolder\table\report.txt"  #or use raw string
print (filepath)

print ("----------------------------------------------------------------")
#multiline string
mystring = """The Olympic Games, often referred to simply as the Olympics, 
is an international multi-sport event featuring summer and winter sports 
competitions in which thousands of athletes from around the world 
participate in a variety of competitions. The Games are considered 
the world's foremost sports competition, with more than 200 nations 
participating. The modern Olympics are held every four years, with 
the Summer and Winter Games alternating by occurring every four years 
but two years apart.""" 
print (mystring)

print ("----------------------------------------------------------------")
#paragraph can be converted into list of words
#split sentences by space character
words = mystring.split()
print (words)
print (len(words))

print ("----------------------------------------------------------------")
#remove spaces in string

print(mystring.replace (" ", ""))
print(mystring.replace ("a", "aaaaa"))
print (mystring.count("a "))
print (mystring.count("the"))
print (mystring.count("ing"))

print ("----------------------------------------------------------------")

mystring = "I bought {0} {1} for {2}"
print (mystring.format (10, "televsion", 5000.55 ))

mystring = "I bought {0:5d} {1:20s} for {2:10.2f}"
print (mystring.format (11, "radio", 3000.55 ))

print ("----------------------------------------------------------------")

intro = ["Hello", "world", "this", "is", "Python"]

print (intro)
print (" ". join (intro))
print ("--------".join(intro)) #Join the list into a single string

print ("----------------------------------------------------------------")

mystring = "      Hello welcome to Python \n"
print (mystring. strip (), "123") #strip has remove "\n"
print (mystring. strip ())        #used to remove any space

