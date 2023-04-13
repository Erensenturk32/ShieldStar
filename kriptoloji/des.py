from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def des_roget(key, plaintext):
    # DES anahtarı 8 byte (64 bit) uzunluğunda olmalıdır.
    # Eğer verilen anahtarın uzunluğu 8 byte'tan kısa ise, eksik kalan kısmı rastgele verilerle tamamlayalım.
    if len(key) < 8:
        key += get_random_bytes(8 - len(key))

    # ECB (Electronic Codebook) modunda bir DES şifreleme objesi oluşturalım.
    crypt = DES.new(key, DES.MODE_ECB)

    # Açık metni 8 byte'lık bloklara bölüp her bir bloku DES ile şifreleyelim.
    # Ayrıca son blok tam 8 byte uzunluğunda değilse, eksik kısmı boşluk karakterleriyle tamamlayalım.
    # Şifrelenmiş her blok, birleştirilerek çıktı olarak döndürülsün.
    crypttest = b''
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8].ljust(8)
        crypttest += crypt.encrypt(block)

    return crypttest

def des_evolve(key, crypttest):
    # DES anahtarı 8 byte (64 bit) uzunluğunda olmalıdır.
    # Eğer verilen anahtarın uzunluğu 8 byte'tan kısa ise, eksik kalan kısmı rastgele verilerle tamamlayalım.
    if len(key) < 8:
        key += get_random_bytes(8 - len(key))

    # ECB (Electronic Codebook) modunda bir DES şifreleme objesi oluşturalım.
    crypt = DES.new(key, DES.MODE_ECB)

    # Şifrelenmiş metni 8 byte'lık bloklara bölüp her bir bloku DES ile deşifreleyelim.
    # Deşifrelenmiş her blok, birleştirilerek çıktı olarak döndürülsün.
    plaintext = b''
    for i in range(0, len(crypttest), 8):
        block = crypttest[i:i+8]
        plaintext += crypt.decrypt(block)

    # Deşifrelenmiş metnin sonunda oluşan boşluk karakterlerini kaldıralım.
    return plaintext.rstrip()

# Örnek kullanım
import os 
anahtar =os.urandom(8)
key = anahtar
#ASCII karakter ile mesaj yazılır
mesaj = input("mesaj yazın : ") 
mesaj = mesaj.encode()
plaintext = mesaj
# Şifreleme işlemi
crypttest = des_roget(key, plaintext)
print("Şifrelenmiş metin:", crypttest.hex())

# Deşifreleme işlemi
decrypted_text = des_evolve(key, crypttest)
print("Deşifrelenmiş metin:", decrypted_text.decode())
