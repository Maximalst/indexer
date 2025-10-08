print("Worker started")


import csv
import os

def read_path_from_csv(file_name="settings.csv"):
    """Liest den Pfad aus einer CSV-Datei mit einer Spalte 'path'."""
    try:
        with open(file_name, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                path = row.get('path')
                if path:
                    return path.strip()
        print("no Path!!.")
        return None
    except FileNotFoundError:
        print(f"Die Datei '{file_name}' wurde nicht gefunden.")
        return None

def main():
    path = read_path_from_csv()
    if path:
        print(f"✅ Pfad aus CSV gelesen: {path}")
        if os.path.exists(path):
            print("📂 Der Pfad existiert auf dem System.")
        else:
            print("⚠️ Der Pfad existiert nicht auf dem System.")
    else:
        print("❌ Kein Pfad verfügbar.")

if __name__ == "__main__":
    main()
