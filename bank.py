import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Bank"
)

mycursor = mydb.cursor()

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    print("Select Gender:")
    print("1. Male")
    print("2. Female")
    print("3. Other")
    gender_choice = input("Enter choice: ")

    if gender_choice == "1":
        gender = "male"
    elif gender_choice == "2":
        gender = "female"
    else:
        gender = "other"

    sql = "INSERT INTO users(username, password, gender) VALUES (%s, %s, %s)"
    val = (username, password, gender)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Registration Successfully Completed!\n")


def login():
    password = input("Enter your password: ")
    username = input("Enter your username: ")

    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    mycursor.execute(sql,(username, password))
    user = mycursor.fetchone()

    if user:
        print("Login Successful! Welcome {username}\n")
    else:
        print("Login Failed. Invalid username or password.\n")


def logout():
    print("Logout Successful.\n")


def main():
    while True:
        print("Welcome to Bank")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")

        choice = input("ENTER CHOICE: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Please enter a valid choice\n")


main()



