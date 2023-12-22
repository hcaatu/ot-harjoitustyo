# Kahvi clicker

Pelin tavoitteena on klikkailla kahvikuvaketta, ostaa päivityksiä ja siten kerryttää entistä enemmän kahvia pankkiin.

Peli toimii samalla Aineopinteojen harjoitustyö: Ohjelmistotekniikka -kurssin projektina. 

![image](https://github.com/hcaatu/ot-harjoitustyo/assets/128474929/950b265f-f275-48db-898c-0c353c229bb8)


## Peliohje
Pelin voi tallentaa painamalla näppäimistöstä S. Peli lataa aikaisemman tallennuksen automaattisesti käynnistäessä. Painamalla G näppäimistöstä saa 1000 scorea, jonka avulla voi testata ominaisuuksia. 

## Dokumentaatio
- [Työtunnit](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/tyotunnit.md)
- [Vaatimusmäärittely](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Asennus- ja käyttöohje

1. Repositorion voi kloonata hakemistoon komennolla

```bash
git clone
```

2. Hakemistoon voi siirtyä komennolla
```bash
cd ot-harjoitustyo
```

3. Sovelluksen riippuvuudet asennetaan komennolla

```bash
poetry install
```

4. Sovellus käynnistetään komennolla

```bash
poetry run invoke start
```

## Muut komennot

### Testaus

Sovelluksen toimivuus on testattu virtuaalityöaseman kautta yliopiston Cubbli Linuxilla. Sekä pelin suorittaminen että muutkin komennon toimivat odotetusti.
Ohjelman testit voi suorittaa ot-harjoitustyo -hakemiston sisällä komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportin saa generoitua komennolla:

```bash
poetry run invoke coverage-report
```

Testauskattavuus on viimeisimmässä versiossa 78%.
 | statements | missing  |  excluded | branches | partial | coverage |
| :----:|:-----| :-----|:-----|:-----|:-----|
| 288 | 49    | 0 | 94| 10|78%|

### Pylint

Tiedoston [.pylintrc](./.pylintrc) mukaiset koodin tarkastukset voidaan suorittaa komennolla:

```bash
poetry run invoke lint
```

Huom. Moduulissa UI on asetettu poikkeus pylint: disable=consider-using-f-string, sillä muuttujan alustaminen ennen f-stringiin sijoittamista korjaa selittämättämän syntax errorin WSL:ssä. Virtuaalityöpöydällä Linuxissa en kohdannut samaa ongelmaa.

Viimeisimmässä versiossa pylint-virheitä on kolme ja komennon ajaminen kertoo seuraavaa:
Your code has been rated at 9.93/10 (previous run: 9.93/10, -0.00)
