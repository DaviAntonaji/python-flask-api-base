from base64 import b64decode, b64encode
from Crypto.Cipher import Blowfish

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'latin1')
unpad = lambda s: s[0:-s[-1]]

class AESCipher:
    def __init__(self, key):
        self.key = bytes(key, 'utf-8')

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        encrypted = cipher.encrypt(raw)
        return b64encode(encrypted)

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        decrypted = cipher.decrypt(enc)
        return unpad(decrypted).decode('latin1')
