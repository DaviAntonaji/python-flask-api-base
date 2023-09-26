
from flask_jwt_extended import create_access_token, get_jwt_identity
import datetime
import base64
import json
from auth import cryptdecrypt

import os
from dotenv import load_dotenv

load_dotenv()



def AccessKey():
    return os.getenv("BLOWFISH_KEY")

def createToken(payload):
    expires = datetime.timedelta(hours=int(os.getenv("TOKEN_HOURS_VALIDATE")))
    token = create_access_token(identity=encodedPayload(payload), expires_delta=expires)

    return token


def encodedPayload(data):
    data = str(data)
    cipher = cryptdecrypt.AESCipher(AccessKey())
    encrypted = cipher.encrypt(data)
    string = encrypted.decode('utf-8').replace("/", "|")
    return string
    

def decodedPayload(data):

    cipher = cryptdecrypt.AESCipher(AccessKey())
    decrypted = cipher.decrypt(data.replace("|", "/"))


    return decrypted

def createFreshToken():
    currentDataToken = decodedPayload(get_jwt_identity())
    currentDataToken = json.loads(currentDataToken)
    freshAccessToken = createToken(json.dumps(currentDataToken))

    return freshAccessToken


