# Trails Challenge

## Overview (Italian)

(See the English below)

**Trails Challenge** è la traduzione letteraria di *Gara dei Sentieri*, un'attività scout organizzata da *A.G.E.S.C.I. Zona di Ancona*.  Consiste in una sfida sulle tecniche scout, a cui partecipano le Squadriglie appartenenti ai Reparti della Zona di Ancona, e si svolge ogni anno in una location differente e dura in genere mezza giornata.

Trails Challenge nasce quindi dall'esigenza degli organizzatori di tenere sotto controllo l'andamento della gara in tempo reale e stilare la classifica immediatamente dopo la chiusura della gara.

In breve:
* ciascuna Squadriglia ha a disposizione una mappa in cui sono segnate le prove
* ogni prova è tenuta da Capi scout che esaminano la Squadriglia su una determinata tecnica scout, assegnandole un voto sulla tecnica (da 1 a 5) e un voto sullo stile scout tenuto durante la prova (da 1 a 5)
* requisiti essenziali per classificarsi sono:
  * fare almeno una tra le prove obbligatorie
  * registrarsi al punto di ritrovo finale entro l'ora stabilita
* ciascuna postazione di prova comunica alla centrale via apparato radio portatile rtx il punteggio assegnato a ciascuna Squadriglia esaminata
* gli operatori di centrale riportano i dati su Trails Challenge e il gioco è fatto!


## Overview

**Trails Challenge** is the literary translation of *Gara dei Sentieri*, a scout activity organized by *AGESCI Zona di Ancona*, the Italian chatolic scout association.  *Gara dei Sentieri* is a challenge on the scout techniques, between Patrols belonging to scout district of Ancona (Italy), and it's organised every year in a different location and usually lasts half a day.

Trails Challenge fills the need of organizers to monitor the race trend in real time and to generate a ranking list immediately after the end of the challenge.

Shortly:
* each patrol has a map which shows the testing stations
* each testing station is organised by scout leaders who examine patrols on a particular scout technique, giving it a vote on the technique (1 to 5) and a vote on the scout style showed during the test (1 to 5)
* there are two mandatory conditions for each patrol:
  * doing at least one of the mandatory tests
  * arriving at the final meeting point within the set time
* each testing station communicates the score assigned to each patrol to the operative central by portable radio rtx or by smartphone
* radio operators, who are in the operative central, report data on Trails Challenge and you're done!


## Technical Overview

Trails Challenge has been developed as an experiment and it was initially used in occasion of the event at Osimo (AN), Italy on March 22, 2015 (results [here](http://trailschallenge.ancona5.it/)).  It has been developed with the best possible effort by some volounteers, without having parametrizations or reuse in mind, so you can expect hard-coded values and tricks in order to just make things happen, even if the big picture is clean enough.  We envite to contribute by opening issues and sending pull requests (for bug reporting/fixing), improvement proposals and new features.

We've an [installation guide](docs/install.md) for production environments, and a [roadmap](docs/roadmap.md) for future releases.

In Trails Challenge we've 4 entities to manage:
* Patrol:  it's a group of 4-5 scouts or guides
* Group:  each patrol belongs to a Scout Group
* Technique:  each test station examines patrols on a particular scout technique
* Test:  it's when a patrol is examined by a test station

Then, there are 5 features:
* Summary:  a list of the statistics of every patrol, ordered by group
* Ranking List:  the ranking list of the patrols
* Techniques Monitor:  list of the techniques, ordered by "popularity"
* Tests Flux:  show all the tests, ordered chronogically (inverted), and it's periodically refreshed
* Add Test:  view for adding tests

Technically, Trails Challenge is basically composed by:
* an API server, built on the top of Django REST Framework and PostgreSQL, who expose RESTful APIs via [JWT](http://jwt.io/)-based authentication
* a SPA built with AngularJS, UI-Router, Restangular, Satellizer, LoDash and CoffeeScript


## Contributors

* Antonio Esposito, Software Developer
* Diego Veccia, Product Manager
* Leonardo Paciotti, Graphic Designer
* Giulia Saccone, Language Consultant


## License

The software is released under the [GNU AGPL v3](LICENSE.md), and the [logo](static/tclogo.svg) under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Trails Challenge relies entirely on Free Software, included the font used in logo, [Sibila](http://openfontlibrary.org/en/font/sibila), released under the [OFL](http://scripts.sil.org/OFL).
