import json

with open("exercises.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    item_id = item.get("id", "").lower()
    name = item.get("name", "").lower()
    
    # Standard auf Bodygewicht
    eq = "Körpergewicht / Freie Übung (Bodyweight)"
    
    # Wichtig: Spezifische Geräte ZUERST prüfen, damit "band" nicht von anderen Regeln überschrieben wird
    if "band" in item_id or "band" in name or "resistance" in item_id:
        eq = "Widerstandsband (Resistance Band)"
    elif "dumbbell" in item_id or name.startswith("dumbbell"):
        eq = "Kurzhantel (Dumbbell)"
    elif "cable" in item_id or name.startswith("cable"):
        eq = "Kabelzug (Cable)"
    elif "barbell" in item_id or name.startswith("barbell"):
        eq = "Langhantel (Barbell)"
    elif "lever" in item_id or "machine" in item_id or "sled" in item_id:
        eq = "Maschine (Lever/Machine)"
    elif "kettlebell" in item_id or "kettlebell" in name:
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

print("Equipment-Regeln erfolgreich priorisiert und korrigiert!")
