# Kahvi clicker

Pelin tavoitteena on klikkailla kahvikuvaketta, ostaa päivityksiä ja siten kerryttää entistä enemmän kahvia pankkiin.

Peli toimii samalla Aineopinteojen harjoitustyö: Ohjelmistotekniikka -kurssin projektina. 

## Peliohje
Pelin voi tallentaa painamalla näppäimistöstä S. Painamalla G näppäimistöstä saa 1000 scorea, jonka avulla voi testata ominaisuuksia.

## Dokumentaatio
- [Työtunnit](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/tyotunnit.md)
- [Vaatimusmäärittely](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/hcaatu/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Release 1](https://github.com/hcaatu/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

1. Riippuvuudet asennetaan komennolla

```bash
poetry install
```

2. Sovellus käynnistetään komennolla

```bash
poetry run invoke start
```

## Muut komennot

### Testaus

Ohjelman testaus tapahtuu suorittamalla komento:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin saa generoitua komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedoston [.pylintrc](./.pylintrc) mukaiset koodin tarkastukset voidaan suorittaa komennolla:

```bash
poetry run invoke lint
```
