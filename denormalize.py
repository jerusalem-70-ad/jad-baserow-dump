import json
import os

from config import JSON_FOLDER
from config import DATA_FOLDER


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