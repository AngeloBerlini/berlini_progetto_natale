# Diagramma UML per beta.py

```mermaid
classDiagram
    class Calciatore {
        -String nome
        -String ruolo
        -float abilita
        -int gol
        +Calciatore(String nome, String ruolo, float abilita)
        +sega_gol()
    }

    class Squadra {
        -String nome
        -float forza
        -int punti
        -List~Calciatore~ calciatori
        +Squadra(String nome, float forza)
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