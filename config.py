import os
from acdh_baserow_pyutils import BaseRowClient


BASEROW_DB_ID = 578
BASEROW_URL = "https://baserow.acdh-dev.oeaw.ac.at/api/"
BASEROW_USER = os.environ.get("BASEROW_USER")
BASEROW_PW = os.environ.get("BASEROW_PW")
BASEROW_TOKEN = os.environ.get("BASEROW_TOKEN")
JSON_FOLDER = "json_dumps"
DATA_FOLDER = "data"
TEI_FOLDER = "tei"


try:
    br_client = BaseRowClient(
        BASEROW_USER, BASEROW_PW, BASEROW_TOKEN, br_base_url=BASEROW_URL
    )
except KeyError:
    br_client = None


DENORMALIZE_CONFIG = [
    {
        "table_label": "KEYWORDS",
        "final_file": [DATA_FOLDER, "keywords.json"],
        "fields": [
            {
                "field_name": "part_of",
                "seed_file": [JSON_FOLDER, "keywords.json"],
                "source_file": [JSON_FOLDER, "keywords.json"],
            }
        ]
    },
    {
        "table_label": "INSTITUTIONS",
        "final_file": [DATA_FOLDER, "institutional_context.json"],
        "fields": [
            {
                "field_name": "part_of",
                "seed_file": [JSON_FOLDER, "institutional_context.json"],
                "source_file": [JSON_FOLDER, "institutional_context.json"],
            }
        ]
    },
    {
        "table_label": "Libraries",
        "final_file": [DATA_FOLDER, "libraries.json"],
        "fields": [
            {
                "field_name": "place",
                "seed_file": [JSON_FOLDER, "places.json"],
                "source_file": [JSON_FOLDER, "libraries.json"],
            }
        ]
    },
    {
        "table_label": "WORKS",
        "final_file": [DATA_FOLDER, "works.json"],
        "fields": [
            {
                "field_name": "author",
                "source_file": [JSON_FOLDER, "works.json"],
                "seed_file": [JSON_FOLDER, "authors.json"],
            },
            {
                "field_name": "published_edition",
                "source_file": [DATA_FOLDER, "works.json"],
                "seed_file": [JSON_FOLDER, "sources_occurrences.json"],
            },
            {
                "field_name": "institutional_context",
                "source_file": [DATA_FOLDER, "works.json"],
                "seed_file": [DATA_FOLDER, "institutional_context.json"],
            },
        ]
    },
    {
        "table_label": "MANUSCRIPTS",
        "final_file": [DATA_FOLDER, "manuscripts.json"],
        "fields": [
            {
                "field_name": "library",
                "seed_file": [DATA_FOLDER, "libraries.json"],
                "source_file": [JSON_FOLDER, "manuscripts.json"],
            },
            {
                "field_name": "institutional_context",
                "seed_file": [DATA_FOLDER, "institutional_context.json"],
                "source_file": [DATA_FOLDER, "manuscripts.json"],
            }
        ]
    },
    {
        "table_label": "PASSAGES",
        "final_file": [DATA_FOLDER, "passages.json"],
        "fields": [
            {
                "field_name": "work",
                "seed_file": [DATA_FOLDER, "works.json"],
                "source_file": [JSON_FOLDER, "occurences.json"],
            },
            {
                "field_name": "manuscript",
                "seed_file": [DATA_FOLDER, "manuscripts.json"],
                "source_file": [DATA_FOLDER, "passages.json"],
            },
            {
                "field_name": "keywords",
                "seed_file": [DATA_FOLDER, "keywords.json"],
                "source_file": [DATA_FOLDER, "passages.json"],
            }
        ]
    },
]
