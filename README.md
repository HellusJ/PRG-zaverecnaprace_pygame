<h1 align="center"><br>Kostky v pygame</br></h1>

<h2>Pruběh hry</h2>

<p>Je to lokální multiplayerová hra pro 2 hráče .Po zapnutí hry se vám ukáže menu, ve kterém máte na výběr ze 3 možností:</p>
<ul>
  <li>Play - hrát</li>
  <li>Rules - pravidla</li>
  <li>Quit - ukončí hru</li>
</ul>
<p>Po stisknutí play se přesunete na hrací pole, kde máte oba k dispozici tlačítko "throw", kterým provedete hod. Poté je náhodně vylosováno 6 kostek a nakonec se vám přičtou body za daný hod. Kdo získá jako první 10000 bodů stává se vítězem.</p>

<h2>Kód</h2>

<p>Tento kód dělá hru s názvem "Kostky" pomocí Pygame. Po inicializaci Pygame nastaví herní okno a definuje několik funkcí, jako je menu(), rules(), a hra(). Hra začíná v menu, kde si hráč může vybrat mezi hraním, zobrazením pravidel a ukončením hry. Ve funkci hra() hráči střídavě házejí kostkami a získávají body podle specifických pravidel. Funkce animace_ruk() a animace_ruk_opp() zobrazují animace rukou při házení kostkami. Zvuky jsou přehrávány pomocí funkce zvuk(), která načítá a hraje zvukové soubory pro různé akce ve hře. Celý kód běží v cyklu, který čeká na uživatelské vstupy, jako je kliknutí myší.</p>
