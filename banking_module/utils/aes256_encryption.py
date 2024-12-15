from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import hashlib


def derive_key(key):
    """Derives a 32-byte key from a passphrase using SHA-256."""
    return hashlib.sha256(key.encode('utf-8')).digest()


def aes_encrypt(data, key):
    """
    Encrypts data using AES-256 encryption.
    
    :param data: Data to be encrypted (string).
    :param key: Passphrase to derive 32-byte encryption key.
    :return: Encrypted data (base64 encoded).
    """
    key = derive_key(key)
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(iv + encrypted_data).decode('utf-8')


def aes_decrypt(encoded_data, key):
    """
    Decrypts data using AES-256 decryption.
    
    :param encoded_data: Base64-encoded encrypted data.
    :param key: Passphrase to derive 32-byte decryption key.
    :return: Decrypted data (string).
    """
    key = derive_key(key)
    encrypted_data = base64.b64decode(encoded_data)
    iv = encrypted_data[:AES.block_size]
    encrypted_content = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_content), AES.block_size)
    return decrypted_data.decode('utf-8')


# Example Usage:
# passphrase = "securepassword123"  # Any length passphrase
# message = "Oleksandr Merkulov"

# # Encrypt the message
# encrypted_message = aes_encrypt(message, passphrase)
# print(f"Encrypted: {encrypted_message}")

# # Decrypt the message
# decrypted_message = aes_decrypt(encrypted_message, passphrase)
# print(f"Decrypted: {decrypted_message}")
