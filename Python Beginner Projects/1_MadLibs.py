''' A mad Libs project is a fun word game where users provide random words (such as nouns, verbs,
and adjective), which are then inserted into a pre-written story template to create humorous or
unexpected results.'''

#a few ways to concatenate string:
#YouTuber = input("Give me the name: ")
# print("Subscribe to " + YouTuber)
# print("Subscribe to {}".format(YouTuber))
# print(f"Subscribe to {YouTuber}")

adj = input("Adjective: ")
verb = input("Verb: ")
adverb = input("Adverb: ")
famous_man = input("Person: ")
noun = input("Noun: ")

madlib = f"Computer programming is so {adj}! It makes us to {verb} {adverb}. \
There is a computer algorithm named after a computer scientist is \
called {famous_man} algorithm. This algorithm helps us to make lots of {noun}."

print(f"Our Madlib: {madlib}")