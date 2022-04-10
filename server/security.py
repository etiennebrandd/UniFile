import hashlib
import uuid
from cryptography.fernet import Fernet
import time
import jwt
import re
from io import StringIO
from html.parser import HTMLParser

# Generate a  for any encryption
# key = Fernet.generate_key()
key = b'LPltkdHU304flx_T9Jlx1VYJpGmycdardnH4itSspP0='
fernet = Fernet(key)

# Can be used to return a SHA-256 hash of input
# X (bool) used to indicate salt should be generated
# Y (string) used for passing in pre-made salt
def hash(message, x, y):

    # If hash is requested with salt
    if x == True:

        # Generate UUID
        salt = uid()
        # Input is message concat w/ salt
        input = (message + salt).encode()

        hash = hashlib.sha256(input).hexdigest()

        return hash, salt

    elif(x == False and y != ""):

        # Passed in salt is the salt (duh)
        salt = y
        # Input is message concat w/ salt
        input = (message + salt).encode()

        hash = hashlib.sha256(input).hexdigest()
        return hash

    else:

        # No salt to be generated or passed in
        salt = ""

        # Input is just message
        input = message.encode()

        hash = hashlib.sha256(input).hexdigest()
        return hash


# Can be used to generate a UUID for salting or cookie
def uid():

    id = uuid.uuid4()
    
    return id.hex


# Encrypt a plaintext
# def encrypt(plaintext):
    
#     ciphertext = fernet.encrypt(str.encode(plaintext))
#     return ciphertext


# # Decrypt a ciphertext
# def decrypt(ciphertext):

#     plaintext = fernet.decrypt(ciphertext).decode()
#     return plaintext


def generateJWT(userDetails):

    # UserDetails dict of details to store in jwt

    # Need to fetch current time and add 6 hours
    currentTime = int(time.time())
    expTime = currentTime + 21600

    # Assemble the payload
    payload = {
        "usr": userDetails["fname"] + " " + userDetails["lname"],
        "lvl": userDetails["tier"],
        "tmz": userDetails["timezone"],
        "thm": userDetails["theme"],
        "exp": expTime
    }

    # Assemble the JWT
    encodedJWT = jwt.encode(payload, key, algorithm="HS256")
    splitJWT = re.split("\.", encodedJWT)
    sig = splitJWT[2]

    # Return whole JWT, expiry time, and signature
    return encodedJWT, expTime, sig


# Decode token
def decodeJWT(token):

    decodedJWT = jwt.decode(token, key, algorithms=["HS256"])
    
    name = re.split(" ", decodedJWT["usr"])

    return name[0]


# Class to strip HTML
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def inputValidator(data):

    s = MLStripper()
    s.feed(data)
    data = s.get_data()

    return data
