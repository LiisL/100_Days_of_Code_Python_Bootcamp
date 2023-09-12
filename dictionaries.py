programming_dictionary = {}
programming_dictionary["Loop"] = "A loop is a software program or script that repeats the same instructions or processes the same information over and over until receiving the order to stop."
programming_dictionary["Regex"] = "Short for regular expression"
programming_dictionary["Binary"] = "Binary is a base-2 number system invented by Gottfried Leibniz"


for key in programming_dictionary:
    print(key)
    programming_dictionary[key] = "Changed text"
print(programming_dictionary)