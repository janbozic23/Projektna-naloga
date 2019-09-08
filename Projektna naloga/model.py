import os.path

class User:
    def __init__(self, ime, priimek, username, password, email):
        self.firstname = ime
        self.lastname = priimek
        self.username = username
        self.password = password
        self.email = email
        if not os.path.exists('files\{}_izpisek.txt'.format(self.username)):    #preveri ali file obstaja, sicer ga naredi
            with open('files\{}_izpisek.txt'.format(self.username), 'w+') as _:     #dodas: encoding="utf-8"
                pass
            with open('files\{}_balance.txt'.format(self.username), 'w+') as data:
                print('0', file = data)
        self.account = Bank_account(self.username)

    def __str__(self):
        return 'Vaše uporabniško ime je {}'.format(self.username)

    def __repr__(self):
        return 'User({}, {}, {}, {}, {})'.format(self.firstname, self.lastname, self.username, self.email, self.password)

    def register(self):
        with open('users.txt', 'a') as data:
            print('{}, {}, {}, {}, {}'.format(self.firstname, self.lastname, self.username, self.password, self.email), file = data)

    def izvedi_transakcijo(self, transakcija):
        if transakcija.expense:
            self.account.stanje -= transakcija.amount
        else:
            self.account.stanje += transakcija.amount
        with open(self.account.izpisek, 'a') as data:
            print(transakcija, file = data)
        with open('files\{}_balance.txt'.format(self.username), mode = 'w') as data:
            print(self.account.stanje, file = data)

    def __eq__(self, other):
        return self.username == other.username



class Bank_account:
    def __init__(self, username):
        with open('files\{}_balance.txt'.format(username), 'r') as data:
            for vrstica in data:
                stevilka = float(vrstica.strip())
                self.stanje = stevilka
                break
        self.izpisek = 'files\{}_izpisek.txt'.format(username)
    
    def __str__(self):
        return 'Na vašem računu je {} €.'.format(self.stanje)

    def __repr__(self):
        return 'Na vašem računu je {}€.'.format(self.stanje)    


    
class Transaction:
    def __init__(self, amount, note, expense = True):
        self.amount = amount
        self.expense = expense
        self.note = note
        
    def __str__(self):
        if self.expense:
            return 'Strošek v višini {} €, opomba: {}'.format(self.amount, self.note)
        else:
            return 'Prihodek v višini {} €, opomba: {}'.format(self.amount, self.note)

def pridobi_uporabnike(txt_file):
    #nabere vse uporabnike iz podane datoteke in jih zmeče v seznam, ki ga vrne
    seznam = []
    with open(txt_file, 'r', encoding = 'utf-8') as data:
        for vrstica in data:
            seznamcek = vrstica.strip().split(', ')
            seznam.append(User(*seznamcek))
    return seznam

def free_username(seznam, username):
    #preveri, ali je uporabniško ime že zasedeno
    for el in seznam:
        if el.username == username:
            return False
    return True

def free_email(seznam, email):
    #preveri ali je email že zaseden
    for el in seznam:
        if el.email == email:
            return False
    return True

def valid_email(seznam, email):
    #preveri ali je email v pravem formatu
    if '@' not in email or '.' not in email or len(email) < 6:
        return False
    else:
        return '@.' not in email and '.@' not in email and email[0] not in '.@' and email[-1] not in '.@'

def valid_geslo(geslo):
    #preveri ali je geslo veljavno
    for el in geslo:
        if el in '1234567890':
            return len(geslo) > 7
    return False

def je_stevilka(stevilka):
    #preveri string in ugotovi, ali je številka
    for el in stevilka:
        if el not in '1234567890.':
            return False
    return stevilka.count('.') <= 1 and len(stevilka) > 0

