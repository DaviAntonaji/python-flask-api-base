from base64 import b64decode
from base64 import b64encode
from hashlib import md5
from Crypto.Cipher import Blowfish


BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'latin1')
unpad = lambda s : s[0:-ord(s[-1:])]

class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')
        

    def encrypt(self, raw):
        raw = pad(raw)
        
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        return b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('latin1')
