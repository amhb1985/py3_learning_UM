#
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []

for word in words:
    if word.endswith("e"):
        past_tense.append(word + "d")
    else:
        past_tense.append(word + "ed")

print("Past tense words:", past_tense)

#exersize:
