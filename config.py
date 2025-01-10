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
ID_FIELD = "jad_id"
DEFAULT_DELETE_FIELDS = [
    "$..order",
]


try:
    br_client = BaseRowClient(
        BASEROW_USER, BASEROW_PW, BASEROW_TOKEN, br_base_url=BASEROW_URL
    )
except KeyError:
    br_client = None


MODEL_CONFIG = [
    {
        "table_label": "AUTHORS",
        "label_lookup_expression": "$.name",
        "final_file": [DATA_FOLDER, "authors.json"],
        "orig_file": "authors.json",
        "fields": [],
    },
    {
        "table_label": "BIBL-REFS",
        "label_lookup_expression": "$.name",
        "final_file": [DATA_FOLDER, "biblical_references.json"],
        "orig_file": "biblical_references.json",
        "fields": [],
    },
    {
        "table_label": "CLUSTER",
        "label_lookup_expression": "$.name",
        "final_file": [DATA_FOLDER, "clusters.json"],
        "orig_file": "cluster.json",
        "fields": [],
    },
    {
        "table_label": "DATE",
        "label_lookup_expression": "$.name",
        "final_file": [DATA_FOLDER, "dates.json"],
        "orig_file": "date.json",
        "fields": [],
    },
    {
        "table_label": "LITURGICAL-REFS",
        "label_lookup_expression": "$.name",
        "final_file": [DATA_FOLDER, "liturgical_references.json"],
        "orig_file": "liturgical_references.json",
        "fields": [],
    },
    {
        "table_label": "SOURCE-OCCURRENCE",
        "label_lookup_expression": "$.name",
        "final_file": [DATA_FOLDER, "sources_occurrences.json"],
        "orig_file": "sources_occurrences.json",
        "fields": [],
    },
    {
        "table_label": "KEYWORDS",
        "label_lookup_expression": "$.name",
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
        "label_lookup_expression": "$.name",
        "final_file": [DATA_FOLDER, "institutional_contexts.json"],
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
        "label_lookup_expression": "$.name",
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
        "label_lookup_expression": "$.name",
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
                "seed_file": [DATA_FOLDER, "institutional_contexts.json"],
            },
        ]
    },
    {
        "table_label": "MANUSCRIPTS",
        "label_lookup_expression": "$..name[0].value",
        "final_file": [DATA_FOLDER, "manuscripts.json"],
        "fields": [
            {
                "field_name": "library",
                "seed_file": [DATA_FOLDER, "libraries.json"],
                "source_file": [JSON_FOLDER, "manuscripts.json"],
            },
            {
                "field_name": "institutional_context",
                "seed_file": [DATA_FOLDER, "institutional_contexts.json"],
                "source_file": [DATA_FOLDER, "manuscripts.json"],
            }
        ]
    },
    {
        "table_label": "PASSAGES",
        "label_lookup_expression": "$.passage",
        "final_file": [DATA_FOLDER, "passages.json"],
        "fields": [
            {
                "field_name": "work",
                "seed_file": [DATA_FOLDER, "works.json"],
                "source_file": [JSON_FOLDER, "occurrences.json"],
            },
            {
                "field_name": "keywords",
                "seed_file": [DATA_FOLDER, "keywords.json"],
                "source_file": [DATA_FOLDER, "passages.json"],
            },
        ]
    },
    {
        "table_label": "MS-OCCURRENCES",
        "label_lookup_expression": "$..occurrence[0].value",
        "final_file": [DATA_FOLDER, "ms_occurrences.json"],
        "orig_file": "ms_occurrences.json",
        "fields": [],
    },
]
