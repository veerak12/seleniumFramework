from faker import Faker

def generate_random_email():
    # Create an instance of the Faker class
    fake = Faker()

    # Generate a random email
    random_email = fake.email()

    return random_email

# Example usage:
# if __name__ == "__main__":
#     random_email = generate_random_email()
#     print("Random Email:", random_email)