current_users = ['glidebomb', 'admin', 'fatpussy', 'nob0dy', 'gate13']
new_users = ['Sierra69', 'DoLoReS', 'JohnQ', 'nob0dy', 'Gate13']

for user in new_users:
    if user.lower() in current_users:
        print(user + " will need to enter a new username.")
    else:
        print("Username " + user + " is available.")

