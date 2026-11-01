import json

with open("exercises.json", "r", encoding="utf-8") as f:
    data = json.load(f)

equipment_rules = [
    ("band", "Widerstandsband (Resistance Band)"),
    ("cable", "Kabelzug (Cable)"),
    ("lever", "Maschine (Lever/Machine)"),
    ("dumbbell", "Kurzhantel (Dumbbell)"),
    ("barbell", "Langhantel (Barbell)"),
    ("smith", "Multipresse (Smith Machine)"),
    ("kettlebell", "Kugelhantel (Kettlebell)"),
    ("assisted", "Maschine mit Unterstützung (Assisted Machine)"),
    ("weighted", "Zusatzgewicht (Weighted)"),
    ("sled", "Schlitten (Sled/Leg Press)"),
    ("roller", "Faszienrolle / Ab Roller"),
    ("rope", "Seil (Rope Cable)"),
]

updated_count = 0
for item in data:
    item_id = item.get("id", "").lower()
    item_name = item.get("name", "").lower()
    
    matched_eq = None
    for kw, eq_name in equipment_rules:
        if kw in item_id or kw in item_name:
            matched_eq = eq_name
            break
            
    if not matched_eq:
        matched_eq = "Körpergewicht / Freie Übung (Bodyweight)"
        
    item["equipment"] = matched_eq
    p_muscle = item.get("primary_muscle", item.get("folder", "Muskelgruppe"))
    item["description_de"] = (
        f"Übung: {item.get('name')} | "
        f"Benötigtes Equipment: {matched_eq}. "
        f"Beanspruchte Muskeln: {p_muscle}. "
        f"Führe die Bewegung kontrolliert im vollen Bewegungsumfang aus, "
        f"um den optimalen Trainingseffekt zu erzielen."
    )
    updated_count += 1

with open("exercises.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Fertig! Equipment und Beschreibungen für {updated_count} Übungen wurden korrigiert.")
