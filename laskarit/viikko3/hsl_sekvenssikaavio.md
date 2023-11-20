## HSL maksukorttiluokan sekvenssikaavio


```mermaid
sequenceDiagram
    participant main
    participant Kioski
    participant Lataajalaite
    participant Lukijalaite
    participant Matkakortti
    participant HKLLaitehallinto

    main ->> HKLLaitehallinto: HKLLaitehallinto()

    main ->> HKLLaitehallinto: lisaa_lataaja(rautatietori)
    main ->> HKLLaitehallinto: lisaa_lukija(ratikka6)
    main ->> HKLLaitehallinto: lisaa_lukija(bussi244)

    
    main ->> Kioski: osta_matkakortti("Kalle")
    activate Kioski
    Kioski -->> main: Matkakortti("Kalle")
    deactivate Kioski

    main ->> Lataajalaite: lataa_arvoa(kallen_kortti, 3)
    Lataajalaite ->> Matkakortti: kasvata_arvoa(3)

    main ->> Lukijalaite: osta_lippu(kallen_kortti, 0)
    activate Lukijalaite
    Lukijalaite ->> Matkakortti: vahenna_arvoa(1.5)
    Lukijalaite -->> main: True
    deactivate Lukijalaite

    main ->> Lukijalaite: osta_lippu(kallen_kortti, 2)
    activate Lukijalaite
    Lukijalaite -->> main: False
    deactivate Lukijalaite
```
