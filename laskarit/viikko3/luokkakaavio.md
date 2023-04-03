Monopoli havainnollistettuna luokkakaaviona:

```mermaid
 classDiagram
      Noppa ..> Nappula
      Pelaaja -- Nappula
      Nappula ..> Ruutu
      Ruutu .. Pelaaja
      
      class Ruutu{
          ruutu id
          ruudun nimi
          hinta
          kuka omistaa
          seuraava ruutu
      }
      class Pelaaja{
          id
          nimi
          nappula
          saldo
          kiinteistöt
      }    
      
      class Noppa{
          silmäluku
          nappula id
      }
      
      class Nappula{
          pelaaja
          nykyinen ruutu
          seuraava ruutu
      }
      
```
