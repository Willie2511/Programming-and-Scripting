rawstring = input("Please Enter A String: ")
normalisedstring = rawstring.strip().lower()

length_of_rawstring = len(rawstring)
length_of_normalisedstring = len(normalisedstring)

print("That string normalised is: {}".format(normalisedstring))
print("We reduced the input string from {} to {} chharacters".format(length_of_rawstring, length_of_normalisedstring))
