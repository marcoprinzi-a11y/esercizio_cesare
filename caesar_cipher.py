def encrypt(text: str, key: int) -> str:
    """
        Cifra il testo usando il Cifrario di Cesare.
        Per decifrare, passare il valore negativo della chiave (-key).
        """
    result = ""

    for char in text:
        # Controlliamo se il carattere è una lettera dell'alfabeto
        if char.isalpha():
            # Determiniamo il valore di normalizzazione (ASCII 'A' o 'a')
            start = 65 if char.isupper() else 97

            # 1. Convertiamo in ASCII con ord()
            # 2. Normalizziamo a 0-25 sottraendo lo start
            # 3. Applichiamo la formula (valore + chiave) % 26
            # 4. Riportiamo in ASCII aggiungendo lo start
            # 5. Riconvertiamo in carattere con chr()
            new_char = chr((ord(char) - start + key) % 26 + start)
            result += new_char
        else:
            # Se non è una lettera (spazio, punteggiatura), resta invariato
            result += char
    return result

def main():
        print("--- Cifrario di Cesare ---")

        # Scelta dell'operazione
        scelta = input("Vuoi (C)ifrare o (D)ecifrare? ").upper()

        if scelta not in ['C', 'D']:
            print("Scelta non valida. Riavvia il programma.")
            return

        # Acquisizione input
        messaggio = input("Inserisci il testo: ")
        try:
            chiave = int(input("Inserisci la chiave (numero intero): "))
        except ValueError:
            print("Errore: la chiave deve essere un numero intero.")
            return

        # Se l'utente vuole decifrare, usiamo il negativo della chiave
        if scelta == 'D':
            risultato = encrypt(messaggio, -chiave)
        else:
            risultato = encrypt(messaggio, chiave)

        # Output finale
        print(f"\nRisultato: {risultato}")

if __name__ == "__main__":
    main()