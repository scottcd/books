# Check if a user is NOT in the list
banned_users = ['andrew', 'carolina', 'david']\
user = 'lilly'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')