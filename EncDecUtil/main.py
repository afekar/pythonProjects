from cryptography.fernet import Fernet
import rsa
import os


def Symmetric_key_gen():
    cipher_key = Fernet.generate_key()
    return cipher_key


def Symmetric_encrypt(key, message):
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(message)
    return encrypted_text


def Symmetric_decrypt(key, ciphertext):
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text


def symmetric_enc(filename):
    with open(filename, 'rb') as f:
        text = f.read()
    key = Symmetric_key_gen()
    ciphertext = Symmetric_encrypt(key, text)
    return ciphertext, key


def symmetric_dec(filename, keypath):
    with open(filename, 'rb') as f:
        ciphertext = f.read()
    with open(f"{keypath}\keys\{filename}\key.txt", 'rb') as f:
        key = f.read()
    decrypted = Symmetric_decrypt(key, ciphertext)
    return decrypted


def asymmetric_enc(filename):
    with open(filename, 'rb') as f:
        text = f.read()
    (pubkey, privkey) = rsa.newkeys(2048)
    pubkey_pem = pubkey.save_pkcs1()  # (format='PEM')
    privkey_pem = privkey.save_pkcs1()
    ciphertext = rsa.encrypt(text, pubkey)
    return ciphertext, pubkey_pem, privkey_pem


def asymmetric_dec(filename, keypath):
    with open(filename, 'rb') as f:
        ciphertext = f.read()
    with open(f"{keypath}\keys\{filename}\privkey.pem") as privatefile:
        keydata = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(keydata, 'PEM')
    decrypted = rsa.decrypt(ciphertext, privkey)
    return decrypted

def enc_dir(path, keypath, mode):
    content = os.listdir(path)
    dirs = []
    files = []
    temp = [os.path.join(path, child) for child in content]
    for item in temp:
        if os.path.isdir(item):
            dirs.append(item)
        else:
            files.append(item)
    if mode == 0:
        for item in files:
            ciphertext, key = symmetric_enc(item)
            with open(item, 'wb') as f:
                f.write(ciphertext)
            if not os.path.exists(f"{keypath}\keys\{item}"):  # create folders if not exists
                os.makedirs(f"{keypath}\keys\{item}")
            with open(f"{keypath}\keys\{item}\key.txt", 'wb') as f:
                f.write(key)
        for item in dirs:
            enc_dir(item, keypath, mode)
    else:
        for item in files:
            ciphertext, pubkey, privkey = asymmetric_enc(item)
            with open(item, 'wb') as f:
                f.write(ciphertext)
            if not os.path.exists(f"keys\{item}"):  # create folders if not exists
                os.makedirs(f"keys\{item}")
            with open(f"keys\{item}\pubkey.pem", 'wb') as f:
                f.write(pubkey)
            with open(f"keys\{item}\privkey.pem", 'wb') as f:
                f.write(privkey)
        for item in dirs:
            enc_dir(item, keypath, mode)


def dec_dir(path, keypath, mode):
    content = os.listdir(path)
    dirs = []
    files = []
    temp = [os.path.join(path, child) for child in content]
    for item in temp:
        if os.path.isdir(item):
            dirs.append(item)
        else:
            files.append(item)
    if mode == 0:
        for item in files:
            text = symmetric_dec(item, keypath)
            with open(item, 'wb') as f:
                f.write(text)
        for item in dirs:
            dec_dir(item, keypath, mode)
    else:
        for item in files:
            text = asymmetric_dec(item, keypath)
            with open(item, 'wb') as f:
                f.write(text)
        for item in dirs:
            dec_dir(item, keypath, mode)


def main():
    print('Укажите путь к директории, которую необходимо зашифровать/дешифровать: ')
    path = str(input())
    print("Укажите режим работы: 0 - шифрование, 1 - дешифрование")
    mode = int(input())
    print("Укажите тип алгоритма шифрования/дешифрования: 0 - симметричный, 1 - асимметричный: ")
    flag = int(input())
    print("Форма сохранения/загрузки ключей шифрования/дешифрования: 0 - файл, 1 - токен")
    type = int(input())
    if type==0 and mode==0:
        print("Укажите путь для сохранения файла с ключами: ")
    elif type==1 and mode==0:
        print("Укажите путь для сохранения ключа на токен: ")
    if type == 0 and mode == 1:
        print("Укажите путь до файла с ключами дешифрования: ")
    elif type == 1 and mode == 1:
        print("Укажите путь для ключей дешифрования на токене: ")
    keypath = str(input())
    if os.path.exists(f"{keypath}\keys"):
        pass
    else:
        os.makedirs(f"{keypath}\keys")
    if mode == 0:
        enc_dir(path, keypath, flag)
    else:
        dec_dir(path, keypath, flag)


if __name__ == "__main__":
    main()
