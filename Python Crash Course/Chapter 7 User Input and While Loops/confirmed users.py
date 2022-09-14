unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    confirm_users = unconfirmed_users.pop()

    print(f"Verifying user: {confirm_users.title()}")
    confirmed_users.append(confirm_users)

print("The following users have been verified:")
for confirmed_users in confirmed_users:
    print(confirmed_users.title()
          )