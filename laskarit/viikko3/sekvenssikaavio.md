```mermaid
    sequenceDiagram
        participant main
   
        main->>Machine: Machine()
        Machine->>Tank: FuelTank()
        Machine->>Tank: fill("40")
        Machine->>Tank: Engine("Tank")
        main->>Machine: drive()
        Machine->>Engine: start()
        Engine-->>Tank: consume(5)
        Machine->>Engine: use_energy()
        Engine-->>Tank: consume(10)

        
