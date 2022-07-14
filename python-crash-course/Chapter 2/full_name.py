# Sometimes, it is useful to use a 
# variable value in a string. This
# technique is called f-strings.
first_name = "chandler"
last_name = "scott"

# f-string line here:
full_name = f"{first_name} {last_name}"

print(full_name)
print(f'Hello, {full_name.title()}')