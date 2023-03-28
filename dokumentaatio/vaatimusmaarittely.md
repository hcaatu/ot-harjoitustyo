# Vaatimusmäärittely

## Yleiskuvaus

Sovellus on yksinkertainen Tower defence -peli pygamella.

## Käyttäjät

Sovelluksen käyttäjärooleja ovat tavallinen käyttäjä eli pelaaja sekä kehittäjä, jolla on enemmän oikeuksia, kuten pelin vaikeustason säätäminen ja koodien käyttäminen.

## Suunnitellut toiminnallisuudet

### Pelin idea

Pelaajan tarkoitus on rakentaa *torneja*, jotka hyökkäävät itsestään vihollista kohti siten, ettei vihollinen pääse matkustamaan kartan läpi *tukikohtaan* saakka. Peli etenee kierroksittain jatkuvasti haastavammin. Pelaaja häviää, jos viholliset pääsevät matkustamaan *tukikohtaan* liian useasti. 

### Pelin toiminnallisuus

- Pelissä on yksinkertainen graafinen käyttöliittymä, joka on toteutettu pygamen avulla.
- Pelaaja pystyy sijoittamaan valikosta *torneja* kartalle. 
- Tornit hyökkäävät vihollista kohti, kun ne ovat tietyn etäisyyden päässä tornista.
- Viholliset liikkuvat kartalla ennalta määrättyä reittiä pitkin kohti *tukikohtaa*.
- Pelaaja kerää *valuuttaa* tuhottuja vihollisia kohden. 
- Pelaajan *tukikohdalla* on tietty määrä kestävyyttä, ja kun vihollinen osuu siihen, se menettää kestävyyttä.

## Ideoita jatkokehitykseen

- teemaidea: Viholliset ovat *bugeja* ja tornit koodareita, jotka ampuvat *koodisädettä* tuhotakseen bugit. 
- Erilaisia torneja, jotka hyökkäävät eri tavoin.
- Erilaisia helpompia ja vaikeampia vihollisia. 
- Muutama erilainen kartta
- Ennätystaulukko peliin

