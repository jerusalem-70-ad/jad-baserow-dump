import json
import os

from config import JSON_FOLDER
from config import DATA_FOLDER


print("KEYWORDS")
final_file = os.path.join(DATA_FOLDER, "keywords.json")
source_file = os.path.join(JSON_FOLDER, "keywords.json")
with open(source_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

print("  - part_of")
seed_file = os.path.join(JSON_FOLDER, "keywords.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["part_of"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["part_of"] = new_values

print(f"  saving KEYWORDS as {final_file}")
with open(final_file, "w", encoding="utf-8") as f:
    json.dump(source_data, f, ensure_ascii=False, indent=2)

print("INSTITUTIONS")
final_file = os.path.join(DATA_FOLDER, "institutional_context.json")
source_file = os.path.join(JSON_FOLDER, "institutional_context.json")
with open(source_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

print("  - part_of")
seed_file = os.path.join(JSON_FOLDER, "institutional_context.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["part_of"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["part_of"] = new_values

print(f"  saving INSTITUTIONS as {final_file}")
with open(final_file, "w", encoding="utf-8") as f:
    json.dump(source_data, f, ensure_ascii=False, indent=2)

print("LIBRARIES")
final_file = os.path.join(DATA_FOLDER, "libraries.json")
source_file = os.path.join(JSON_FOLDER, "libraries.json")
with open(source_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

print("  - place")
seed_file = os.path.join(JSON_FOLDER, "places.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["place"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["place"] = new_values

print(f"  saving LIBRARIES as {final_file}")
with open(final_file, "w", encoding="utf-8") as f:
    json.dump(source_data, f, ensure_ascii=False, indent=2)


print("WORKS")
final_file = os.path.join(DATA_FOLDER, "works.json")
source_file = os.path.join(JSON_FOLDER, "works.json")
with open(source_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

print("  - author")
seed_file = os.path.join(JSON_FOLDER, "authors.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["author"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["author"] = new_values

print("  - published_edition")
seed_file = os.path.join(JSON_FOLDER, "sources_occurrences.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["published_edition"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["published_edition"] = new_values

print("  - institutional_context")
seed_file = os.path.join(DATA_FOLDER, "institutional_context.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["institutional_context"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["institutional_context"] = new_values

print(f"  saving WORKS as {final_file}")
with open(final_file, "w", encoding="utf-8") as f:
    json.dump(source_data, f, ensure_ascii=False, indent=2)


print("MANUSCRIPTS")
final_file = os.path.join(DATA_FOLDER, "manuscripts.json")
source_file = os.path.join(JSON_FOLDER, "manuscripts.json")
with open(source_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

print("  - library")
seed_file = os.path.join(DATA_FOLDER, "libraries.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["library"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["library"] = new_values

print("  - institutional_context")
seed_file = os.path.join(DATA_FOLDER, "institutional_context.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["institutional_context"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["institutional_context"] = new_values

print(f"  saving MANUSCRIPTS as {final_file}")
with open(final_file, "w", encoding="utf-8") as f:
    json.dump(source_data, f, ensure_ascii=False, indent=2)


print("PASSAGES")
final_file = os.path.join(DATA_FOLDER, "passages.json")
source_file = os.path.join(JSON_FOLDER, "occurences.json")
with open(source_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

print("  - work")
seed_file = os.path.join(DATA_FOLDER, "works.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["work"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["work"] = new_values

print("  - work")
seed_file = os.path.join(DATA_FOLDER, "works.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["work"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["work"] = new_values

print("  - manuscript")
seed_file = os.path.join(DATA_FOLDER, "manuscripts.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["manuscript"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["manuscript"] = new_values

print("  - keywords")
seed_file = os.path.join(DATA_FOLDER, "keywords.json")
with open(seed_file, "r", encoding="utf-8") as f:
    seed_data = json.load(f)
for key, value in source_data.items():
    old_values = value["keywords"]
    new_values = []
    for x in old_values:
        new_values.append(seed_data[f"{x['id']}"])
    value["keywords"] = new_values

print(f"  saving PASSAGES as {final_file}")
with open(final_file, "w", encoding="utf-8") as f:
    json.dump(source_data, f, ensure_ascii=False, indent=2)
