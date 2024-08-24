password = "1234"
balance = 100000
new_password = None

choices = ["1. Withdraw","2. Deposit","3. Check Balance","4. Reset Password","5. Exit"]
for i in choices:
    print(i)
    print()

user_choice = int(input("Enter Your choice: "))

if user_choice == 1:
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    user_password = input("Enter Your password: ")

    if user_password == password:

        if withdraw_amount < 1500:
            print("Keep atleast 1500 rs as minimum balance")
            print(f"Your current balance is {balance} rs")

        else:
            balance -= withdraw_amount
            print(f"Your current balance is {balance} rs")

    else:
        print("Password incorrect")

elif user_choice == 2:
    dep_amount = int(input("Enter the amount to deposit: "))
    balance += amount
    print(f"Your current balance is {balance} rs")

elif user_choice == 3:
    print(f"Your balance is {balance} rs")

elif user_choice == 4:
    new_password == input("Enter new password: ")
    password = new_password
    print("Password changed successfully")

elif user_choice == 5:
    print("Thank You")

else:
    print("Enter the correct choice\nTry again ")





























