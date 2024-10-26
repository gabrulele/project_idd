import os
import json

def analizza_tutti_json(cartella_json):
    
    # Inizializza variabili per le statistiche globali
    totale_tabelle = 0
    totale_references = 0
    totale_json = 0
    tabelle_senza_references = 0
    tabelle_senza_caption = 0
    tabelle_senza_footnotes = 0

    # Lista dei file JSON nella cartella specificata
    for file in os.listdir(cartella_json):
        if file.endswith(".json"):
            totale_json += 1
            file_path = os.path.join(cartella_json, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            numero_tabelle = len(data)
            totale_tabelle += numero_tabelle

            # Cicla su ogni tabella per calcolare le statistiche
            for id_tabella, dettagli in data.items():
                references = dettagli.get('references', [])
                footnotes = dettagli.get('footnotes', [])
                caption = dettagli.get('caption', None)

                # Controlla le tabelle senza references
                if len(references) == 0:
                    tabelle_senza_references += 1

                # Controlla le tabelle senza caption
                if caption is None or caption.strip() == "":
                    tabelle_senza_caption += 1

                # Controlla le tabelle senza footnotes
                if len(footnotes) == 0:
                    tabelle_senza_footnotes += 1

                # Conta il numero totale di references
                totale_references += len(references)

    # Calcola le statistiche finali
    numero_medio_tabelle_per_json = totale_tabelle / totale_json if totale_json > 0 else 0
    numero_medio_references_per_tabella = totale_references / totale_tabelle if totale_tabelle > 0 else 0
    percentuale_tabelle_senza_references = (tabelle_senza_references / totale_tabelle * 100) if totale_tabelle > 0 else 0
    percentuale_tabelle_senza_caption = (tabelle_senza_caption / totale_tabelle * 100) if totale_tabelle > 0 else 0
    percentuale_tabelle_senza_footnotes = (tabelle_senza_footnotes / totale_tabelle * 100) if totale_tabelle > 0 else 0

    # Restituisce i risultati
    return {
        "totale_tabelle": totale_tabelle,
        "numero_medio_tabelle_per_json": numero_medio_tabelle_per_json,
        "numero_medio_references_per_tabella": numero_medio_references_per_tabella,
        "tabelle_senza_references": tabelle_senza_references,
        "percentuale_tabelle_senza_references": percentuale_tabelle_senza_references,
        "tabelle_senza_caption": tabelle_senza_caption,
        "percentuale_tabelle_senza_caption": percentuale_tabelle_senza_caption,
        "tabelle_senza_footnotes": tabelle_senza_footnotes,
        "percentuale_tabelle_senza_footnotes": percentuale_tabelle_senza_footnotes
    }

# Esempio di utilizzo
cartella_json = "homework_1/extraction"  # Modifica il percorso se necessario
risultati = analizza_tutti_json(cartella_json)

# Stampa i risultati
print(f"Numero totale di tabelle: {risultati['totale_tabelle']}")
print(f"Numero medio di tabelle per JSON: {risultati['numero_medio_tabelle_per_json']:.2f}")
print(f"Numero medio di references per tabella: {risultati['numero_medio_references_per_tabella']:.2f}")
print(f"Numero di tabelle senza references: {risultati['tabelle_senza_references']}")
print(f"Percentuale di tabelle senza references: {risultati['percentuale_tabelle_senza_references']:.2f}%")
print(f"Numero di tabelle senza caption: {risultati['tabelle_senza_caption']}")
print(f"Percentuale di tabelle senza caption: {risultati['percentuale_tabelle_senza_caption']:.2f}%")
print(f"Numero di tabelle senza footnotes: {risultati['tabelle_senza_footnotes']}")
print(f"Percentuale di tabelle senza footnotes: {risultati['percentuale_tabelle_senza_footnotes']:.2f}%")