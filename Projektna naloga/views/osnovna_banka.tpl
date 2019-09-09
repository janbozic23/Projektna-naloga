%rebase('osnova.tpl')


<section class="hero is-info is-fullheight">
  <div class="hero-head">
    <nav class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item">
            BOŽANSKA BANKA
          </a>
          <span class="navbar-burger burger" data-target="navbarMenuHeroB">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </div>
        <div id="navbarMenuHeroB" class="navbar-menu">
          <div class="navbar-end">
            <span class="navbar-item">
              <a>

                        <form action='/izpis/'>
            <input type='submit' class="button is-focused is-info is-inverted" value='Odjava'>
            </form>
              </a>
            </span>
          </div>
        </div>
      </div>
    </nav>
  </div>

  <div class="hero-body">
    <div class="container has-text-centered">
      <p class="title">
            Dobrodošli {{ime}}!
      </p>
      <p class="subtitle">
        {{prijavljen.account}}
      </p>
    </div>
  </div>

  <div class="hero-foot">
    <nav class="tabs is-boxed is-fullwidth">
      <div class="container">
        <ul>
          <li>
             <a><form action='/zgodovina/'>
            <input type='submit' class="button is-focused is-info is-inverted" value='Zgodovina transakcij'>
        </form></a>
          </li>
          <li>
            <a>        <form action='/transakcija/'>
            <input type='submit' class="button is-focused is-info is-inverted" value='Izvedi transakcijo'>
        </form></a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</section>
