from tqdm import tqdm
from config import br_client, BASEROW_DB_ID
from pylobid.pylobid import PyLobidPerson

TEMP_FILE = "temp.json"

current_table = br_client.get_table_by_name(BASEROW_DB_ID, "authors")
gnd_id_schema = "https://d-nb.info/gnd/{}"


items = []
filters = {"filter__field_31791__contains": "http", "filter__field_39479__empty": True}
for x in br_client.yield_rows(current_table, filters=filters):
    item = x
    items.append(item)


enriched = {}
for x in tqdm(items, total=len(items)):
    payload = {}
    ent_id = x["id"]
    gnd = x["gnd_url"]
    person_item = PyLobidPerson(gnd)
    ent_dict = person_item.ent_dict
    enriched[ent_id] = ent_dict
    alt_names = " | ".join(ent_dict["variantName"])
    payload["alt_name"] = alt_names
    try:
        payload["date_of_birth"] = "".join(ent_dict["dateOfBirth"])
    except KeyError:
        pass
    try:
        payload["date_of_death"] = "".join(ent_dict["dateOfDeath"])
    except KeyError:
        pass
    update = br_client.patch_row(current_table, ent_id, payload)
