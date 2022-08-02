# 5.1 Capitalize the word stating with m:
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

song = song.replace(" m", " M")

print(song)

# 5.2 Print each list question with its correctly matching answer
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
    ]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
    ]

print(questions[0])
print(answers[1] + '\n')

print(questions[1])
print(answers[2] + '\n')

print(questions[2])
print(answers[0] + '\n')
