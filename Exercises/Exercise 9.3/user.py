class User:
    """An attmpt to model a user profile"""

    def __init__(self, first_name, last_name, contact, email):

        self.first_name = first_name
        self.last_name = last_name
        self.contact= contact
        self.email = email

    def describe_user(self):
        print("Your name is: " + self.first_name.title() + " " + self.last_name.title()+ ".")
        print("Your contact is: " + str(self.contact)+ ".")
        print("Your email address is: " + self.email +".\n")


user_1 = User("Arthur", "Kariuki", 121212, 'arthurkariuki81@gmail.com')
user_1.describe_user()

user_2 = User("Clark", "Kent", 454545, 'clarkkent......')
user_2.describe_user()