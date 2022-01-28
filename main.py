import accounts
total_ids = accounts.accounts
ids = list(total_ids.keys())
passwords = list(total_ids.values())

# print(ids)
# print(passwords)

print("*****WELCOME TO ONLINE STORES*****")
print("To create account, press [1]")
print("To login into your account, press [2]")

num = int(input("Your number: "))

if num == 1:
    new_id = input("Enter your name: ")
    new_pwd = input("Enter your password: ")
    total_ids[new_id] = new_pwd
    with open('accounts.py', 'w') as f:
        f.write(f"accounts = {str(total_ids)}")

elif num == 2:
    login_user = input("Your name please: ")
    login_pwd = input("Your password please: ")

    if (login_user in ids) and (login_pwd in passwords):
        print("Successfully logged into ONLINE STORES!!!")
    else:
        print(" No account found or Invalid login/password")
else: 
    print("Invalid action!")