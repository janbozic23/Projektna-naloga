%rebase('osnova.tpl')

<div class="container is-widescreen">
  <div class="notification">
       <h1 class="title">Zgodovina transakcij</h1>
  </div>
</div>

<div align="center">
<br>
%with open(prijavljen.account.izpisek, 'r') as data:
%    for vrstica in data:
{{vrstica}} <br>
%end
<br>

<form action='/osnovna_stran/'>
    <input type='submit' class="button is-focused is-info is-inverted" value='Nazaj'>
</form>
<div align="center">
