from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

"""
Esse método vai receber uma public key e uma mensagem a ser encriptada com a lib
"""
def encrypt(pubKey, message):
    # criando o encriptador, no caso está sendo instanciado um que ira performar usando PKCS#1 OAEP
    encryptor = PKCS1_OAEP.new(pubKey)

    # De fato encriptando a mensagem
    # obs: precisei chamar metodo .encode na mensagem
    encrypted = encryptor.encrypt(message.encode())

    return encrypted


"""
    Assim que o programa começar a ser executado, esse método será chamado, e ele sera o responsável por
    executar o código que mostrará a funcionalidade da lib pycryptodome para RSA 
"""
def my_encryption():
    # criando o keyPair que vai ser usado para criar as chaves assimétricas: public e private
    keyPair = RSA.generate(3072)

    # com o keypair anterior, conseguimos criar uma public key e uma private key abaixo
    public_key = keyPair.publickey()
    private_key = keyPair.exportKey()

    # chamando o método responsável por ecriptar uma certa mensage. No caso, estou mandando a public_key que
    # foi gerada anteriormente, e uma mensagem de teste
    msg_encrypted = encrypt(public_key, "Aula sobre SRA")
