import hashlib
import uuid

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

    elif(x == False and y != ""):

        # Passed in salt is the salt (duh)
        salt = y
        # Input is message concat w/ salt
        input = (message + salt).encode()

    else:

        # No salt to be generated or passed in
        salt = ""

        # Input is just message
        input = message.encode()

    # Generates SHA-256 hash of input
    hash = hashlib.sha256(input).hexdigest()

    return hash, salt


# Can be used to generate a UUID for salting or cookie
def uid():

    id = uuid.uuid4()
    
    return id.hex
