# Diagramma UML per main.py

```mermaid
classDiagram
    class Calciatore {
        -Str nome
        -Str ruolo
        -float abilita
        -int gol
        +segna_gol()
    }

    class Squadra {
        -Str nome
        -float forza
        -int punti
        -int vittorie
        -int pareggi
        -int sconfitte
        -List~Calciatore~ calciatori
        +aggiungi_punti(int punti)
        +aggiungi_calciatore(Calciatore calciatore)
    }

    class Campionato {
        -List~Squadra~ squadre
        +aggiungi_squadra(Squadra squadra)
        +simulazione()
        +classifica() List~Squadra~
        +visualizza_classifica()
        +visualizza_classifica_marcatori()
    }

    Calciatore "11" --> "1" Squadra : appartengono a
    Squadra "20" --> "1" Campionato : partecipano a
