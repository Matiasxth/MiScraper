# mi_scraper/storage.py
import csv
import json
import os

def save_to_csv(filename, list_of_dicts):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    Cada clave del diccionario será una columna.
    """
    if not list_of_dicts:
        print("No hay datos para guardar en CSV.")
        return

    fieldnames = list_of_dicts[0].keys()

    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for data in list_of_dicts:
            writer.writerow(data)

def save_to_json(filename, data):
    """
    Guarda los datos en un archivo JSON.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
