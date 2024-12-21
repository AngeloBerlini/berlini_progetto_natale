import matplotlib.pyplot as plt
import random

class Calciatore:
    def __init__(self, nome, ruolo, abilita):
        self.nome = nome
        self.ruolo = ruolo
        self.abilita = abilita
        self.gol = 0

    def segna_gol(self):
        self.gol += 1

class Squadra:
    def __init__(self, nome, forza):
        self.nome = nome
        self.forza = forza
        self.punti = 0
        self.calciatori = []

    def aggiungi_punti(self, punti):
        self.punti += punti

    def aggiungi_calciatore(self, calciatore):
        self.calciatori.append(calciatore)

class Campionato:
    def __init__(self):
        self.squadre = []
    
    def aggiungi_squadra(self, squadra):
        # Controlla se il nome della squadra è già presente
        if any(s.nome == squadra.nome for s in self.squadre):
            print(f"Errore: La squadra '{squadra.nome}' è già stata aggiunta.")
        else:
            self.squadre.append(squadra)
    
    def simulazione(self):
        for giornata in range(1, 39):  # 38 giornate
            print(f"Giornata {giornata}:")
            squadre_giocato = set()
            for turno in range(10):  # 10 partite per giornata
                while True:
                    squadra_casa, squadra_trasferta = random.sample(self.squadre, 2)
                    if squadra_casa.nome not in squadre_giocato and squadra_trasferta.nome not in squadre_giocato:
                        squadre_giocato.add(squadra_casa.nome)
                        squadre_giocato.add(squadra_trasferta.nome)
                        break

                # Simula un risultato basato sulla forza delle squadre
                gol_casa = int(random.gauss(squadra_casa.forza, 1))
                gol_trasferta = int(random.gauss(squadra_trasferta.forza, 1))

                # Assicurati che i gol non siano negativi
                gol_casa = max(0, gol_casa)
                gol_trasferta = max(0, gol_trasferta)

                # Simula i gol dei calciatori
                marcatori_casa = []
                marcatori_trasferta = []
                for _ in range(gol_casa):
                    calciatore = random.choice(squadra_casa.calciatori)
                    calciatore.segna_gol()
                    marcatori_casa.append(calciatore.nome)
                for _ in range(gol_trasferta):
                    calciatore = random.choice(squadra_trasferta.calciatori)
                    calciatore.segna_gol()
                    marcatori_trasferta.append(calciatore.nome)

                # Aggiorna i punti delle squadre e stampa il risultato
                if gol_casa > gol_trasferta:
                    squadra_casa.aggiungi_punti(3)
                    print(f"{squadra_casa.nome} ha vinto {gol_casa}-{gol_trasferta} contro {squadra_trasferta.nome}. Marcatori: {', '.join(marcatori_casa)}")
                elif gol_casa < gol_trasferta:
                    squadra_trasferta.aggiungi_punti(3)
                    print(f"{squadra_trasferta.nome} ha vinto {gol_trasferta}-{gol_casa} contro {squadra_casa.nome}. Marcatori: {', '.join(marcatori_trasferta)}")
                else:
                    squadra_casa.aggiungi_punti(1)
                    squadra_trasferta.aggiungi_punti(1)
                    print(f"{squadra_casa.nome} ha pareggiato {gol_casa}-{gol_trasferta} con {squadra_trasferta.nome}. Marcatori: {', '.join(marcatori_casa + marcatori_trasferta)}")
            print()

    def classifica(self):
        # Ordina le squadre in base ai punti
        classifica_finale = sorted(self.squadre, key=lambda squadra: squadra.punti, reverse=True)
        return classifica_finale

    def visualizza_classifica(self):
        # Ottieni la classifica finale
        classifica_finale = self.classifica()

        # Grafica della classifica finale
        squadre = [squadra.nome for squadra in classifica_finale]
        punti = [squadra.punti for squadra in classifica_finale]

        plt.figure(figsize=(10, 6))
        plt.barh(squadre, punti, color='skyblue')
        plt.xlabel('Punti')
        plt.title('Classifica finale del campionato')
        plt.gca().invert_yaxis()
        plt.show()

        # Salva il grafico
        plot_filename = 'classifica_finale.png'
        plt.savefig(plot_filename)
        print(f"Il grafico è stato salvato come {plot_filename}")

    def visualizza_classifica_marcatori(self):
        # Ottieni la classifica dei marcatori
        marcatori = []
        for squadra in self.squadre:
            for calciatore in squadra.calciatori:
                if calciatore.gol > 0:  # Considera solo i calciatori che hanno segnato almeno un gol
                    marcatori.append((calciatore.nome, calciatore.gol))

        # Ordina i marcatori in base ai gol e prendi i primi 20
        classifica_marcatori = sorted(marcatori, key=lambda x: x[1], reverse=True)[:20]

        # Grafica della classifica marcatori
        nomi = [marcatore[0] for marcatore in classifica_marcatori]
        gol = [marcatore[1] for marcatore in classifica_marcatori]

        plt.figure(figsize=(10, 6))
        plt.barh(nomi, gol, color='lightgreen')
        plt.xlabel('Gol')
        plt.title('Classifica marcatori')
        plt.gca().invert_yaxis()
        plt.show()

        # Salva il grafico
        plot_filename = 'classifica_marcatori.png'
        plt.savefig(plot_filename)
        print(f"Il grafico è stato salvato come {plot_filename}")

# Funzione per chiedere i nomi delle squadre
def chiedi_squadre():
    campionato = Campionato()
    nomi_squadre = set()
    for i in range(20):
        while True:
            nome_squadra = input(f"Inserisci il nome della squadra {i+1}: ")
            if nome_squadra in nomi_squadre:
                print("Il nome della squadra è già stato inserito. Inserisci un nome diverso.")
            else:
                nomi_squadre.add(nome_squadra)
                forza = random.uniform(0.5, 1.5)  # Forza della squadra
                squadra = Squadra(nome_squadra, forza)
                
                # Creazione dei calciatori per ogni squadra
                for j in range(11):  # Ogni squadra ha 11 calciatori
                    ruolo = random.choice(["Attaccante", "Centrocampista", "Difensore"])
                    abilita = random.uniform(0.1, 0.9)  # Probabilità di segnare (abilità)
                    calciatore = Calciatore(f"Giocatore {j+1} {nome_squadra}", ruolo, abilita)
                    squadra.aggiungi_calciatore(calciatore)
                
                campionato.aggiungi_squadra(squadra)
                break
    return campionato

# Esecuzione del programma
campionato = chiedi_squadre()
campionato.simulazione()
campionato.visualizza_classifica()
campionato.visualizza_classifica_marcatori()