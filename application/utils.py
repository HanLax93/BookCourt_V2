import base64
import datetime
import os
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms


def get_input(ui):
    ret = ui.text() if len(ui.text()) != 0 else \
        ui.placeholderText()
    return ret


def log(logmsg: str):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = "logs/" + today + ".log"
    if not os.path.exists("logs"):
        os.mkdir("logs")
    with open(filename, 'a') as f:
        logtime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S',)
        f.write(logtime + " (local time):    " + logmsg + '\n\n')
        f.close()


def get_key(d, value):  # query the serial number of court with its stadium id
    k = [k for k, v in d.items() if v == value]
    return k


class cryptCBCPkcs7(object):  # signature the timestamp

    def __init__(self, key: str, iv: str):
        self.ciphertext = " "
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.iv = iv.encode('utf-8')

    def encrypt(self, text: str):
        cryptor = AES.new(self.key, self.mode, self.iv)

        text = text.encode('utf-8')
        text = self.pkcs7_padding(text)
        self.ciphertext = cryptor.encrypt(text)

        return base64.b64encode(self.ciphertext)

    @staticmethod
    def pkcs7_padding(data):  # padding the data to encrypt
        if not isinstance(data, bytes):
            data = data.encode()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        return padded_data
