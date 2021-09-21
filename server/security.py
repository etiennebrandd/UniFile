import hashlib
import uuid
from cryptography.fernet import Fernet

# Generate a  for any encryption
key = Fernet.generate_key()
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
def encrypt(plaintext):
    
    ciphertext = fernet.encrypt(str.encode(plaintext))
    return ciphertext


# Decrypt a ciphertext
def decrypt(ciphertext):

    plaintext = fernet.decrypt(ciphertext).decode()
    return plaintext

