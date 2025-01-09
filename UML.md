# Diagramma UML per main.py

```mermaid
classDiagram
    class Calciatore {
        -Str nome
        -Str ruolo
        -float abilita
        -int gol
        +Calciatore(String nome, String ruolo, float abilita)
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
        +Squadra(Str nome, float forza)
        +aggiungi_punti(int punti)
        +aggiungi_calciatore(Calciatore calciatore)
    }

    class Campionato {
        -List~Squadra~ squadre
        +Campionato()
        +aggiungi_squadra(Squadra squadra)
        +simulazione()
        +classifica() List~Squadra~
        +visualizza_classifica()
        +visualizza_classifica_marcatori()
    }

    Calciatore --> Squadra : appartiene a
    Squadra --> Campionato : partecipa a
