%rebase('osnova.tpl')

<div class="container is-widescreen">
  <div class="notification">
       <h1 class="title">Prijava</h1>
  </div>
</div>

<div align="center">
%if napaka =='user':
    Uporabniško ime ne obrstaja! <br>
%elif napaka =='pas':
    Napačno geslo! <br>
%end


<form action='/preveri_vpis/' method ="post">
Vpišite vaše uporabniško ime:     
<input class="input" type="text" name='username' placeholder="Uporabniško ime"> <br>
Vpišite vaše geslo:
<input class="input" type="password" name='password' placeholder="Geslo"> <br>

<br>
<input type='submit' class="button is-focused is-info is-inverted" value='Vpiši me'>

</form>
</div>