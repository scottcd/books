name = 'lilly'
message = f"Hi {name.title()}, I hope you are doing well!"

print(message)

##

print(f'{message.lower()}\n{message.upper()}\n{message.title()}')

##

print('My friend said, "We do it!"')

##

famous_person = "Albert Einstein"
quote = 'A person who never made a mistake never tried anything new.'
message = f'{famous_person} said, "{quote}"'

print(message)

##
name = '\nsomething\t'
print(f'{name.lstrip()}\n{name.rstrip()}\n{name.strip()}')