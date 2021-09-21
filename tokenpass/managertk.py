
from flask_jwt_extended import create_access_token, get_jwt_identity
import datetime
import base64
import json
from tokenpass import cryptdecrypt

import os
from dotenv import load_dotenv
from database.connection import connectionDb

load_dotenv()



def AccessKey():
    return os.getenv("BLOWFISH_KEY")

def createToken(payload):
    #expires = datetime.timedelta(hours=72)
    expires = datetime.timedelta(days=2400)
    token = create_access_token(identity=encodedPayload(payload), expires_delta=expires)

    return token


def encodedPayload(data):

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


