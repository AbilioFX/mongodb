"""Random Password Generator."""
import string
import secrets
import uuid

def main(strLength):
    """Generate a secure random string of letters, digits and special characters """
    password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + str(uuid.uuid4())
    return ''.join(secrets.choice(password) for i in range(strLength))

if __name__ == "__main__":
    pw = main(12)
    print(pw)
