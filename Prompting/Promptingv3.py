from sys import argv

script, user1, user2 = argv
prompt = '> '
print(f"""Hi {user1} and {user2}.!
I'd like to ask some random questions.
what do you do at your spare time {user1}?
""")
string = input(prompt)
print(f"What about you {user2}?")
str = input(prompt)

print(f"""
Wow that's really cool so {user1} you like {string}.
and {user2} you like {str}.""")
