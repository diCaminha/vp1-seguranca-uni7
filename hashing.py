import hashlib


def hashing(message_one, message_two):
    m = hashlib.sha256()
    m.update(message_one)
    m.update(message_two)
    return m.digest()

