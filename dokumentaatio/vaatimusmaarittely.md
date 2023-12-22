# Määrittelydokumentti

## Yleiskuvaus

Sovellus on yksinkertainen clicker-peli Pygamella. Pelin ideana on klikkailla ruudulla näkyvää kahvikuppia, joka kerryttää pelaajan pisteitä. 
Pisteillä voi ostaa päivityksiä, jotka kerryttävät entistä enemmän pisteitä. Tavoitteena on kerryttää aina yhä enemmän scorea, ja katsoa kuinka luku ylänurkassa kasvaa.


### Pelin toiminnallisuus

Pelissä on pygamella toteutettu graafinen käyttöliittymä, eli ikkuna, jossa näkyy:
- klikattava kahvikuppi, joka muuttaa kokoa hiiren lähestyessä ja klikattaessa tuottaa pieniä putoavia partikkeleita
- pelaajan score, sekä score per second
- valikkonappia klikkaamalla saa näkyviin ostettavat päivitykset, jotka ovat
  	1. aluksi mustattu, jos pelaaja ei ole vielä saavuttanut niiden ostamiseen vaadittavaa summaa
  	2. harmaita, jos pelaajalla ei kyseisellä hetkellä ole tarpeeksi scorea niiden hankkimiseen
  	   
Ikkunaan ilmestyy satunnaisesti _kultainen kahvi_, jota klikkaamalla saa suuren määrän valuuttaa.

Pelin edistymisen voi tallentaa painamalla näppäimistöstä S. Tallennettu peli latautuu automaattisesti pelin avatessa. Peli tarkistaa tallennustiedoston olemassaolon, ja tarvittaessa alustaa sen oikeaan formaattiin.
Pelissä voi huijata painamalla näppäimistöstä G, jolloin pelaajan pankkiin lisätään 1000 scorea.

### Laajennettavuus

Pelin upgradet eli päivitykset ovat tallennettu yhteen tiedostoon, johon voi miltei copypastettamalla lisätä uusia upgradeja, muokkaamalla vain niiden hinnan ja niiden tuoton. Pelin UI ja klikkausten tunnistaminen toinivat siten, että ne käyvät läpi kaikki sanakirjasta löytyvät päivitykset, ja asettavat niille paikan ruudulla. Toki uusille päivityksille vaaditaan myös uusi kuvake. 

OHjelmoinnissa olen myös yrittänyt välttää arvojen kovakoodaamista, sen sijaan olen pyrkinut alustamaan jokaiselle luokalle arvot konstruktorifunktiossa, jota voidaan kätevästi muuttaa yhdestä paikasta. Kuitenkin järkevässä suhteessa, sillä liian moni attribuutti luokan sisällä huonontaa koodin luettavuutta ja aiheuttaa pylint-virheitä. 

### Kehitysideoita

Peliin voisi lisätä sellaisia päivityksiä, jotka kasvattavat yhdestä klikkauksesta saadun scoren määrää. Tähänkin olen tehnyt alustavat toimenpiteet, mutta en saanut aikaiseksi kuvakkeiden piirtämistä. 

Olin merkinnyt alkuperäiseen vaatimusmäärittelyyn sellaiset päivitykset, jotka muokkaavat pelin ulkoasua, mutta jätin toteuttamatta, sillä ne eivät niinkään laajenna sovelluslogiikkaa vain olisivat vaatineet ainoastaan graafista suunnittelua. Tällaisia päivityksiä olisi kuitenkin edelleen koodin puolesta helposti lisättävissä. 

Myös lisää päivityksiä olisivat esimerkiksi sellaiset, jotka lisäävät _kultaisen kahvin_ ilmestymisen määrää, ja sen klikkauksen pistemäärää. 

Olisin lisännyt vielä peliin uusia partikkeliefektejä, jotka esiintyvät vasta tietyn upgraden ostamisen jälkeen. Näin ulkoasusta olisi tullut monipuolisempi ja pelin pelaamisesta mielenkiintoisempaa.
