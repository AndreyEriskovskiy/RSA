from math import sqrt
from random import choice, randint


class RSA:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.primes = [i for i in range(randint(100, 500), randint(500, 1000) + 1) if self.__is_prime(i)]
        self.__set_keys()


    def __gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.__gcd(b, a % b)

    @staticmethod
    def __is_prime(n):
        if n == 2:
            return True

        if n == 0 or n == 1 or n % 2 == 0:
            return False


        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True

    def __get_rnd_number(self):
        elem = choice(self.primes)
        self.primes.remove(elem)
        return elem

    def __set_keys(self):
        p = self.__get_rnd_number()
        q = self.__get_rnd_number()
        n = p * q
        phi = (p - 1) * (q - 1)

        e = 2
        while self.__gcd(e, phi) != 1:
            e += 1

        self.public_key = (e, n)

        d = 2

        while (d * self.public_key[0]) % phi != 1:
            d += 1

        self.private_key = (d, n)


    def encrypt(self, open_text):

        codes = [ord(char) for char in open_text]

        cipher_text = ''

        e, n = self.public_key

        for code in codes:
            cipher_text += chr(pow(code, e, n))

        return cipher_text


    def decrypt(self, cipher_text):
        codes = [ord(char) for char in cipher_text]

        open_text = ''

        d, n = self.private_key

        for code in codes:
            open_text += chr(pow(code, d, n))

        return open_text


open_text = 'Las Vegas Last April, John took a trip to Las Vegas, Гад блэс, Америка.'
rsa = RSA()

cipher_text = rsa.encrypt(open_text)

decrypted_text = rsa.decrypt(cipher_text)

print(cipher_text.encode('utf-8', errors='ignore').decode('utf-8'))

print(decrypted_text)








