import bottle
import model
from model import User, Bank_account, Transaction
bottle.TEMPLATE_PATH.insert(0, 'views')

seznam = model.pridobi_uporabnike('users.txt')
prijavljen = User('a', 'a', 'a', 'a', 'a')

@bottle.get('/')
def zacetek():
    return bottle.template('zacetna_stran.tpl')

@bottle.get('/registracija/')
def registracija():
    return bottle.template('registracija.tpl', napaka='geslo')

@bottle.post('/preveri_reg/')
def preveri_reg():
    napaka = ''
    ime = bottle.request.forms['ime']
    priimek = bottle.request.forms['priimek']
    uporabnisko = bottle.request.forms['uporabnisko'] 
    geslo1 = bottle.request.forms['geslo1']
    geslo2 = bottle.request.forms['geslo2']
    email = bottle.request.forms['email']
    if len(ime) < 2:
        napaka='ime'
    elif len(priimek) < 2:
        napaka='priimek'
    elif not model.valid_geslo(geslo1):
        napaka = 'geslo1'
    elif geslo1!= geslo2:
        napaka = 'geslo2'
    elif not model.valid_email(seznam, email):
        napaka = 'nev_email'
    elif not model.free_email(seznam, email):
        napaka = 'zas_email'
    elif not model.free_username(seznam, uporabnisko):
        napaka = 'zas_upor'

    if napaka != '':
        return bottle.template('registracija.tpl', napaka = napaka)
    else: 
        uporabnik = User(ime, priimek, uporabnisko, geslo1, email)
        uporabnik.register()
        seznam.append(uporabnik)
        return bottle.template('nazaj_naslovna.tpl', neki = 'Vaša registracija je bila uspešna!')

@bottle.get('/vpis/')
def vpis():
    return bottle.template('vpis.tpl')

@bottle.post('/preveri_vpis/')
def preveri_vpis():
    username = bottle.request.forms['username']
    password = bottle.request.forms['password']
    user = 0
    if  model.free_username(seznam, username):
        return bottle.template('vpis1.tpl', napaka = 'user')
    else: 
        for el in seznam:
            if el.username == username:
                user = el
        if password == user.password:
            global prijavljen
            prijavljen = user
            return bottle.redirect('/osnovna_stran/')
        else:
            return bottle.template('vpis1.tpl', napaka = 'pas')

@bottle.get('/osnovna_stran/')
def osnovna():
    ime = prijavljen.firstname.capitalize() + ' ' + prijavljen.lastname.capitalize()
    return bottle.template('osnovna_banka.tpl', ime = ime, prijavljen = prijavljen)

@bottle.get('/transakcija/')
def transakcija():
    return bottle.template('placilo_priliv.tpl')

@bottle.get('/zgodovina/')
def zgodovina():
    return bottle.template('zgodovina.tpl', prijavljen = prijavljen)

@bottle.get('/izpis/')
def izpis():
    return bottle.template('nazaj_naslovna.tpl', neki = 'Uspešno ste bili izpisani!')

@bottle.get('/placilo/')
def placilo():
    return bottle.template('nakazilo.tpl')

@bottle.post('/preveri_nak/')
def preveri_nak():
    nakazilo = bottle.request.forms['nakazilo']
    opomba = bottle.request.forms['opomba']
    if model.je_stevilka(nakazilo):
        if  prijavljen.account.stanje < float(nakazilo):
            return bottle.template('premalo_denarja.tpl')
        else:
            transakcija = Transaction(float(nakazilo), opomba, True)
            prijavljen.izvedi_transakcijo(transakcija)
            return bottle.redirect('/osnovna_stran/')
    else:
        return bottle.template('narobe.tpl', link = '/placilo/')

@bottle.get('/priliv/')
def priliv():
    return bottle.template('priliv.tpl')

@bottle.post('/preveri_priliv/')
def preveri_priv():
    priliv = bottle.request.forms['priliv']
    opomba = bottle.request.forms['opomba1']
    if model.je_stevilka(priliv):
        transakcija = Transaction(float(priliv), opomba, False)
        prijavljen.izvedi_transakcijo(transakcija)
        return bottle.redirect('/osnovna_stran/')
    else:
        return bottle.template('narobe.tpl', link = '/priliv/')


bottle.run(debug=True, reloader=True)