<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Božanska banka</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>

<div class="container is-widescreen">
  <div class="notification">
       <h1 class="title">Pozdravljeni v Božanski Banki!</h1>
  </div>
</div>

<div align = "center">
    <h2 class="subtitle">{{neki}}</h2>
        <form action='/registracija/'>
            Nišem še registriran uporabnik <br>
            <input type='submit' class="button is-info is-inverted is-focused" value='Želim se registrirati'>
        </form>
        <form action='/vpis/'>
            Sem že registriran uporabnik <br>
            <input type='submit' class="button is-focused is-info is-inverted" value='Želim se vpisati'>
        </form>
</div>
  </body>
</html>