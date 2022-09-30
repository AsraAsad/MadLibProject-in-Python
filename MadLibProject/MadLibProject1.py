# Creating madlib project
# Using f, format stringing in this mini project

#creating variables and asking for user input
# We can put all the nouns and adjectives etc together.
noun_name = input("Noun(Name): ")
noun_place = input("Noun(Place): ")
noun_things1 = input("Noun(Things1): ")
noun_things2 = input("Noun(Things2): ")
adj1 = input("Adjective1: ")
verb1 = input("Verb: ")
verb2 = input("Verb2: ")
verb3 = input("Verb3: ")
verb4 = input("Verb4: ")
verb5 = input("Verb5: ")
verb6 = input("Verb6: ")
verb7 = input("Verb7: ")

# Creating Madlib variable
madlib = f"Hello my name is {noun_name}. I like to do {verb1}. I am so excited to do a {verb2}!\
I am {adj1} person. I want to work in {noun_place}. My passions include {verb3},{verb4}, {verb5}, {verb6}\
 and {verb7}. I want to explore new things like {noun_things1}, {noun_things2} and so on. "

print(madlib)