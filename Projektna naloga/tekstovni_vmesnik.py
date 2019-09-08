from model import User, Bank_account, Transaction
import model



def izbira_username(seznam):
    #uporabink izbere poljubno uporabniško ime, ki še ni zasedeno
    print('Izberite uporabniško ime:')
    odgovor = input('> ')
    if model.free_username(seznam, odgovor):
        return odgovor
    else:
        print('uporabniško ime je že zasedeno.')
        return izbira_username(seznam)

def izbira_password_prva():
    #uporabnik izbira geslo, dokler ne vpiše primernega gesla mu funkcija teži
    print('Izberite vaše geslo. Vsebovati mora vsaj 8 znakov, od tega vsaj eno številko.')
    geslo = input('> ')
    if not model.valid_geslo(geslo):
        print('Neveljavno geslo.')
        return izbira_password_prva()
    else:
        return geslo

def ujemajoc_password(geslo):
    #preveri, ali se geslo ujema s prejšnjim, vrne True/False
    print('Ponovno vpišite izbrano geslo:')
    odgovor = input('> ')
    return odgovor == geslo

def izbira_email(seznam):
    #uporabnik izbere email
    print('Vpišite vaš e-mail:')
    email = input('> ')
    if not model.valid_email(seznam, email):
        print('Vnesli ste neveljaven e-mail.')
        return izbira_email(seznam)
    elif not model.free_email(seznam, email):
        print('Vneseni e-mail je že zaseden.')
        return izbira_email(seznam)
    else:
        return email

def izbira_ime():
    #uporabnik izbere ime
    print('Vpišite vaše ime:')
    ime = input('> ')
    if len(ime) < 2:
        print('Neveljaven vnos')
        return izbira_ime()
    else:
        return ime

def izbira_priimek():
    #uporabnik izbere priimek
    print('Vpišite vaš priimek:')
    ime = input('> ')
    if len(ime) < 2:
        print('Neveljaven vnos')
        return izbira_priimek()
    else:
        return ime

def login_username(seznam):
    #uporabnik vpiše username v loginu
    print('Vpišite vaše uporabniško ime:')
    ime = input('> ')
    if model.free_username(seznam, ime):
        print('Uporabniško ime ne obstaja.')
        return login_username(seznam)
    return ime

def login_password():
    #uporabnik vpiše geslo pri loginu
    print('Vpišite geslo:')
    geslo = input('> ')
    return geslo

def izbira_password():
    #uporabnik izbira geslo med registracijo
    while True:
        geslo = izbira_password_prva()
        if ujemajoc_password(geslo):
            return geslo
        else:
            print('Gesli se ne ujemata.')

def log_in(seznam):
    #uporabnik se vpiše v sistem, vrne primeren objekt razreda User 
    while True:
        username = login_username(seznam)
        user = 0
        for el in seznam:
            if el.username == username:
                user = el
        if login_password() == user.password:
            print('Uspešno ste se prijavili!')
            return user
        else:
            print('Napačno geslo!')
        
def sign_up(seznam):
    #sestavek, kjer se uporabnik registrira
    ime = izbira_ime()
    priimek = izbira_priimek()
    username = izbira_username(seznam)
    password = izbira_password()
    email = izbira_email(seznam)
    uporabnik = User(ime, priimek, username, password, email)
    uporabnik.register()
    seznam.append(uporabnik)
    print('Uspešno ste se registrirali!')

def placilo_ali_priliv():
    #vprasa ali želi denar položiti ali dvigniti
    print('Izberite eno izmed možnosti:')
    print('1) Želim položiti denar')
    print('2) Želim plačati/dvigniti denar')
    odgovor = input('> ')
    if odgovor == '1':
        return False
    elif odgovor == '2':
        return True
    else:
        print('Neveljavna izbira!')
        return placilo_ali_priliv()

def pridobi_amount(user, expense):
    #pridobi znesek plačila in ga vrne
    print('Vpišite količino denarja:')
    odgovor = input('> ')
    if model.je_stevilka(odgovor):
        if expense and user.account.stanje < float(odgovor):
            print('Neveljaven vnos! Nimate dovolj denarja.')
            return pridobi_amount(user, expense)
        else:
            return float(odgovor)
    else:
        print('Neveljaven vnos!')
        return pridobi_amount(user, expense)

def pridobi_note():
    #vpraša uporabnika ali želi kaj zapisati o transakciji, in vrne zapisano
    print('Ali želite dodati kratko opombo?')
    print('1) Da')
    print('2) Ne')
    odgovor = input('> ')
    if odgovor == '1':
        print('Vpišite opombo:')
        opomba = input('> ')
        return opomba
    elif odgovor == '2':
        return '/'
    else:
        print('Neveljaven odgovor!')
        return pridobi_note()

def nova_transakcija(user):
    #pridobi podatke za transakcijo in jo izvede
    placilo = placilo_ali_priliv()
    amount = pridobi_amount(user, placilo)
    note = pridobi_note()
    transakcija = Transaction(amount, note, expense=placilo)
    user.izvedi_transakcijo(transakcija)
    print('Uspešno ste izvedli transakcijo!')

def zgodovina_transakcij(user):
    #izpiše zgodovino transakcij oz izpiske
    with open(user.account.izpisek, 'r') as data:
        for vrstica in data:
            print(vrstica)
    i = input('> ')

def banka(user):
    #osnovni meni znotraj banke
    while True:
        print(user.account)
        print('Izberite eno od možnosti:')
        print('1) Izvedi transakcijo')
        print('2) Preglej zgodovino transakcij')
        print('3) Log out')
        odgovor = input('> ')
        if odgovor == '1':
            nova_transakcija(user)
        elif odgovor == '2':
            zgodovina_transakcij(user)
        elif odgovor == '3':
            break
        else:
            print('Neveljavna izbira!')
        

def main_menu(seznam):
    #osnovni meni
    print('Izberite eno izmed možnosti:')
    print('1) Sem že registriran uporabnik, želim se vpisati!')
    print('2) Nisem še registriran, želim se registrirati!')
    odgovor = input('> ')
    if odgovor == '1':
        user = log_in(seznam)
        banka(user)
    elif odgovor == '2':
        sign_up(seznam)
    else:
        print('Neveljavna izbira!')
        return main_menu(seznam)

def run():
    users = model.pridobi_uporabnike('users.txt')
    while True:
        main_menu(users)

run()