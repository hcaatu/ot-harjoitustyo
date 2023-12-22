# Arkkitehtuurikuvaus

## Pakkauskaavio
:(

## Sekvenssikaavio pelisilmukasta

Kaavio on pitkä, mutta siinä on havainnollistettuna pelisilmukan toiminto yhden silmukan iteraation aikana. Pelisilmukassa on if-lauseita riippuen siitä, mitä syötteitä käyttäjä antaa, joten en ole merkinnyt kaikkea mitä voisi mahdollisesti tapahtua samanaikaisesti tähän kaavioon.

![image](https://github.com/hcaatu/ot-harjoitustyo/assets/128474929/51b2333c-21d4-4e50-8962-b5f4829c0fb8)



## Sekvenssikaavio pelin tallentamisesta
Sekvenssikaavio havainnollistaa, miten eri funktiokutsut etenevät käyttäjän tallentaessa pelin.

```mermaid
sequenceDiagram
    actor User
    participant Main
    participant App
    participant Repository
    User->>Main: click "S" key
    Main->>App: save_game()
    App->>Repository: save(file)
    Repository->>Repository: _write(save_file)
    Repository->>Repository: _ensure_file_exists()
    Repository->>Repository: file.write(data)
    Repository-->>App: save_file
    App-->>Main: file
```
