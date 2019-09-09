%rebase('osnova.tpl')

<div class="container is-widescreen">
  <div class="notification">
       <h1 class="title">Registracija</h1>
  </div>
</div>

<div align="center">
%if napaka == 'ime':
    Neveljavno ime! <br>
%elif napaka == 'priimek':
    Neveljaven priimek! <br>
%elif napaka == 'uporabnisko':
    Izbrano uporabniško ime je že v uporabi. <br>
%elif napaka == 'geslo1':
    Neveljavno geslo! <br>
%elif napaka == 'geslo2':
    Gesli se ne ujemata. <br>
%elif napaka == 'nev_email':
    Vpisam e-mail je neveljaven! <br>
%elif napaka == 'zas_email':
    Vpisan e-mail je že registriran. <br>
%elif napaka == 'zas_upor':
    Izbrano uporabniško ime je že v uporabi! <br>
%end


<form action='/preveri_reg/' method='post'> 
    Vpišite vaše ime: 
    <input class="input" type="text" name='ime' placeholder="Ime"> <br>
    Vpišite vaš priimek: 
    <input class="input" type="text" name='priimek' placeholder="Priimek"> <br>
    Vpišite vaš e-mail:
    <input class="input" type="text" name='email' placeholder="E-mail"> <br>   
    Izberite uporabniško ime: 
    <input class="input" type="text" name='uporabnisko' placeholder="Uporabniško ime"> <br>
    Izberite vaše geslo. Vsebovati mora vsaj 8 znakov, od tega vsaj eno številko. 
    <input class="input" type="password" name='geslo1' placeholder="Geslo"> <br>
    Ponovno vpišite izbrano geslo:
    <input class="input" type="password" name='geslo2' placeholder="Geslo"> <br>
<br>
    <input type='submit' class="button is-focused is-info is-inverted" value='Registracija'>
</form>
</div>