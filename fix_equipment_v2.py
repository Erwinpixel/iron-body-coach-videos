import json

with open("exercises.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item_id = item.get("id", "").lower()
    name = item.get("name", "").lower()
    
    # Standard-Equipment auf Bodyweight setzen
    eq = "Körpergewicht / Freie Übung (Bodyweight)"
    
    # Gezielte Regeln nach ID und echtem Gerät
    if "barbell" in item_id or name.startswith("barbell"):
        eq = "Langhantel (Barbell)"
    elif "dumbbell" in item_id or name.startswith("dumbbell"):
        eq = "Kurzhantel (Dumbbell)"
    elif "cable" in item_id or name.startswith("cable"):
        eq = "Kabelzug (Cable)"
    elif "resistance_band" in item_id or "band" in item_id:
        eq = "Widerstandsband (Resistance Band)"
    elif "lever" in item_id or "machine" in item_id or "sled" in item_id:
        eq = "Maschine (Lever/Machine)"
    elif "kettlebell" in item_id:
        eq = "Kugelhantel (Kettlebell)"
        
    item["equipment"] = eq
    
    p_muscle = item.get("primary_muscle", item.get("folder", "Muskelgruppe"))
    item["description_de"] = (
        f"Übung: {item.get('name')} | "
        f"Benötigtes Equipment: {eq}. "
        f"Beanspruchte Muskeln: {p_muscle}. "
        f"Führe die Bewegung kontrolliert im vollen Bewegungsumfang aus, "
        f"um den optimalen Trainingseffekt zu erzielen."
    )

with open("exercises.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Equipment für alle Übungen erfolgreich neu zugeordnet!")
