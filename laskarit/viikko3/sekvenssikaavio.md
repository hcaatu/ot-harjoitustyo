```mermaid
    sequenceDiagram
        participant main
   
        main->>Machine: Machine()
        Machine->>Tank: FuelTank()
        Machine->>Tank: fill("40")
        Machine->>Tank: Engine("Tank")
