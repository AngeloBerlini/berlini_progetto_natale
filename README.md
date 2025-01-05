# Progetto Campionato di Calcio

Miglioramento del progetto dello scorso anno utilizzando la programmazione a oggetti. Questo progetto simula un campionato di calcio tra 20 squadre. Ogni squadra ha 11 calciatori con abilità diverse. Il programma simula le partite, calcola i punti delle squadre e visualizza la classifica finale e la classifica dei marcatori.

Il progetto include anche un diagramma UML(UML.md)

## Struttura del Progetto

Il progetto è composto dalle seguenti classi principali:

### Classe `Calciatore`

Rappresenta un calciatore con le seguenti proprietà:
- `nome`: il nome del calciatore
- `ruolo`: il ruolo del calciatore (Attaccante, Centrocampista, Difensore)
- `abilita`: la probabilità di segnare un gol
- `gol`: il numero di gol segnati dal calciatore

Metodi:
- `segna_gol()`: incrementa il numero di gol segnati dal calciatore

### Classe `Squadra`

Rappresenta una squadra con le seguenti proprietà:
- `nome`: il nome della squadra
- `forza`: la forza della squadra
- `punti`: i punti accumulati dalla squadra
- `vittorie`: il numero di vittorie della squadra
- `pareggi`: il numero di pareggi della squadra
- `sconfitte`: il numero di sconfitte della squadra
- `calciatori`: la lista dei calciatori della squadra

Metodi:
- `aggiungi_punti(punti)`: aggiunge punti alla squadra
- `aggiungi_calciatore(calciatore)`: aggiunge un calciatore alla squadra

### Classe `Campionato`

Rappresenta il campionato con le seguenti proprietà:
- `squadre`: la lista delle squadre partecipanti

Metodi:
- `aggiungi_squadra(squadra)`: aggiunge una squadra al campionato
- `simulazione()`: simula le partite del campionato
- `classifica()`: restituisce la classifica finale delle squadre
- `visualizza_classifica()`: visualizza la classifica finale delle squadre
- `visualizza_classifica_marcatori()`: visualizza la classifica dei marcatori

## Utilizzo

### Prerequisiti

Assicurati di avere Python installato sul tuo sistema. Inoltre, installa la libreria `matplotlib` utilizzando il seguente comando:

```sh
pip install matplotlib
```
### Esecuzione del Programma

1.Clona il repository o scarica i file del progetto.
2.Apri un terminale nella directory del progetto.
3.Esegui il programma con il seguente comando:
```sh
python beta.py
```
### Inserimento dei Nomi delle Squadre

Il programma chiederà di inserire i nomi delle squadre. Assicurati che i nomi delle squadre non siano vuoti o contengano solo spazi. Se il nome della squadra è già stato inserito, verrà richiesto di inserire un nome diverso.

### Simulazione del Campionato

Dopo aver inserito i nomi delle squadre, il programma simulerà le partite del campionato. Ogni giornata verrà visualizzata nel terminale con i risultati delle partite e i marcatori.

### Visualizzazione della Classifica
Il programma genererà due grafici:

- classifica_finale.png: la classifica finale delle squadre
- classifica_marcatori.png: la classifica dei marcatori
Questi grafici verranno salvati nella directory di esecuzione del programma.

### Contributi
Se desideri contribuire a questo progetto, sentiti libero di aprire una pull request o segnalare un problema.

### Licenza
Questo progetto è distribuito sotto la licenza MIT. Vedi il file LICENSE per ulteriori dettagli.

