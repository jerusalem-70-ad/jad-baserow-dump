import json
import os
from jsonpath_ng import parse

try:
    from .models import MODEL_CONFIG, ID_FIELD
except ImportError:
    from models import MODEL_CONFIG, ID_FIELD

DATA_DIR = "data"


def read_data():

    os.makedirs(DATA_DIR, exist_ok=True)

    for x in MODEL_CONFIG:
        print(x["verbose_name_pl"])
        jsonpath_expr = parse(x["label_lookup_expression"])
        with open(f"{x['data_source']}.json", "r", encoding="utf-8") as fp:
            data = json.load(fp)
        save_path = os.path.join(DATA_DIR, f'{x["file_name"]}.json')

        # add prev/next
        key_list = sorted(data.keys())
        for i, v in enumerate(key_list):
            prev_item = data[key_list[i - 1]][ID_FIELD]
            try:
                next_item = data[key_list[i + 1]][ID_FIELD]
            except IndexError:
                next_item = data[key_list[0]]
            value = data[key_list[i]]

            value["prev"] = f"{prev_item}.html"
            value["next"] = f"{next_item}.html"

        # add view_labels
        for _, value in data.items():
            try:
                value["view_label"] = jsonpath_expr.find(value)[0].value
            except IndexError:
                continue
        with open(save_path, "w", encoding="utf-8") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)


def add_related_objects():
    for x in MODEL_CONFIG:
        try:
            rel_obj = x["related_objects"]
        except KeyError:
            continue
        save_path = os.path.join(DATA_DIR, f'{x["file_name"]}.json')
        with open(save_path, "r") as fp:
            source_data = json.load(fp)

        for item in rel_obj:
            source_file = item["source_file"]
            lookup_field = item["lookup_field"]

            feed_path = os.path.join(DATA_DIR, f"{source_file}.json")
            with open(feed_path, "r") as fp:
                feed_data = json.load(fp)

            for key, value in source_data.items():
                jad_id = value[ID_FIELD]
                related_items = []
                for _, rel_value in feed_data.items():
                    for m in rel_value[lookup_field]:
                        if m[ID_FIELD] == jad_id:
                            related_items.append(
                                {
                                    ID_FIELD: rel_value[ID_FIELD],
                                    "view_label": rel_value["view_label"],
                                }
                            )
                            break
                value[f"related__{source_file}"] = related_items
        with open(save_path, "w", encoding="utf-8") as fp:
            json.dump(source_data, fp, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    read_data()
    add_related_objects()
