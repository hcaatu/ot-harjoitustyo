Monopoli havainnollistettuna luokkakaaviona:

```mermaid
 classDiagram
      Pelaaja "*" -- "1" Noppa
      Noppa "*" ..  "1" Pelaaja
      class Ruutu{
          ruutu id
          ruudun nimi
          hinta
          kuka omistaa
          next
      }
      class Pelaaja{
          nimi
          nappula
          saldo
          omistus
      }    
      
      class Noppa{
          silmäluku
          nappula id
      }
      
      class Nappula{
          pelaaja
          ruutu
      
