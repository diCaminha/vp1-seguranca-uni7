from cryptography.fernet import Fernet

from hashing import hashing


def enviar(mensagem, segredo, chave):
    msg_hashed = hashing(mensagem, segredo)
    f = Fernet(chave)
    encrypt_msg = f.encrypt( mensagem + msg_hashed)
    return encrypt_msg, msg_hashed


def receber(msg_cifrada, segredo, chave, hash):
    f = Fernet(chave)
    decrypted_msg = f.decrypt(msg_cifrada)
    mensagem_sem_hash = decrypted_msg.replace(hash, "")
    msg_hashed = hashing(mensagem_sem_hash, segredo)

    if msg_hashed == hash:
        return mensagem_sem_hash
    else:
        return None


if __name__ == '__main__':
    mensagem = "Ola mundo"
    segredo = "mysecret"
    chave = Fernet.generate_key()

    msg_cifrada, hash = enviar(mensagem, segredo, chave)
    receber(msg_cifrada=msg_cifrada, segredo=segredo, chave=chave, hash=hash)
