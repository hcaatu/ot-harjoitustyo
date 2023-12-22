# Yksityiskohtia testauksesta

Testauksessa yritin painottaa sovelluslogiikan testausta. Sovelluslogiikkaa oli käytännössä helppoa ja suoraviivaista testata, kun taas pelisilmukan testaamisessa kohtasin enemmän haasteita. 
Testien luomisessa en kuitenkaan halunnut aina kovakoodata tiettyä arvoa assertEqual -lauseen sisälle, esim. ensimmäisen upgraden pitäisi tuottaa aina 10 yksikköä, koska olen miettinyt arvojen muuttamista koodissa jatkossa.
Testikattavuus on viimeisimmässä versiossa 78%.

![image](https://github.com/hcaatu/ot-harjoitustyo/assets/128474929/302a5a85-c679-46eb-bf68-9c7bafc50c17)

Sovellusta ohjelmoitaessa olen kuitenkin testannut pääsääntöisesti manuaalisesti peliä pelaamalla ja testaamalla eri ominaisuuksia.
Tämä lähinnä siitä syystä johtuen, että suurin osa ongelmista ja itseasiasta koodistakin on UI-moduulissa, johon ei testejä tarvinnut kirjoittaa.
Törmäsin kerran bugiin, jossa kahvia klikkaamalla sai aivan liikaa scorea, kuin olisi pitänyt saada. En tiedä mikä tämän aiheutti, mutta en ole pystynyt toistamaan tätä bugia testaamalla.
