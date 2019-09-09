%rebase('osnova.tpl')

<div class="container is-widescreen">
  <div class="notification">
       <h1 class="title">Nakazilo</h1>
  </div>
</div>

<div align="center">
<form action='/preveri_nak/' method='post'>
    Vnesite znesek, ki ga želite nakazati: </h2>
    <input class="input" type="text" name='nakazilo' placeholder="Znesek"> <br>
    Vnesite številko računa, na katerega želite denar nakazati:
    <input class="input" type="text" name='neki' placeholder="Račun"> <br>
    Opomba:
    <input class="input" type="text" name='opomba' placeholder="Opomba"> <br>
    <br>
    <input type='submit' class="button is-focused is-info is-inverted" value='Nadaljuj'>
</form>
</div>

