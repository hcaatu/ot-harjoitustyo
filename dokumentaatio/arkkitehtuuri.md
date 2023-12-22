# Arkkitehtuurikuvaus

## Pakkauskaavio
:(

## Sekvenssikaavio pelisilmukasta

Kaavion avulla on havainnollisestettuna, mitä yhden pelisilmukan iteraation aikana tapahtuu

```mermaid
sequenceDiagram
    actor Main

    Main->>GameLoop: start()
    create participant pygame.time.Clock
    GameLoop->>pygame.time.Clock: create pygame.time.Clock
    create participant App
    GameLoop->>App: create App
    create participant Repository
    App->>Repository: create Repository
    create participant AppUI
    GameLoop->>AppUI: create AppUI
    create participant pygame.window
    AppUI->>pygame.window: create pygame.window
    create participant Golden
    GameLoop->>Golden: create Golden
    create participant EventHandler
    GameLoop->>EventHandler: create EventHandler

    GameLoop->>App: load_game()
    App->>Repository: load()
    Repository->>Repository: _read()
    Repository-->>App: loaded_file
    App->>App: _calculate_profit()

    GameLoop->>GameLoop: sync()
    GameLoop->>EventHandler: handle_events()

    EventHandler->>EventHandler: handle_keyboard_inputs()
    EventHandler->>EventHandler: handle_mouse_inputs()
    EventHandler->>AppUI: render_motion_elements()

    GameLoop->>AppUI: fill_screen()
    AppUI->>pygame.window: fill(grey)

    GameLoop->>AppUI: render_text()
    AppUI->>pygame.window: blit(counter)
    AppUI->>pygame.window: blit(score_per_second)

    GameLoop->>AppUI: render_elements()
    AppUI->>pygame.window: blit(images)
    AppUI->>AppUI: black_out_upgrades()

    GameLoop->>Golden: generate()
    Golden-->>GameLoop: pos
    GameLoop->>AppUI: render_golden_coffee()
    
    
    GameLoop->>App: apply_profit()
    GameLoop->>pygame.window: update()
    GameLoop->>pygame.time.Clock: tick(60)
    
    
    

```

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
