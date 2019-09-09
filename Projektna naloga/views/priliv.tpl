%rebase('osnova.tpl')

<div class="container is-widescreen">
  <div class="notification">
       <h1 class="title">Priliv</h1>
  </div>
</div>

<div align="center">
<form action='/preveri_priliv/' method='post'>
    Vnesite znesek, ki si ga želite nakazati:
    <input class="input" type="text" name='priliv'> <br>
    Vnesite številko računa, iz katerega želite denar nakazati:
    <input class="input" type="text" name='neki'> <br>
    Opomba:
    <input class="input" type="text" name='opomba1'> <br>
    <br>
    <input type='submit' class="button is-focused is-info is-inverted" value='Nadaljuj'>
</form>
</div>