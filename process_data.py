import os

from config import DATA_FOLDER, MODEL_CONFIG, ID_FIELD, DEFAULT_DELETE_FIELDS
from utils import add_view_labels, denormalize, add_prev_next, add_related_objects, remove_fields


os.makedirs(DATA_FOLDER, exist_ok=True)

denormalize(MODEL_CONFIG)
add_view_labels(MODEL_CONFIG, ID_FIELD)
add_prev_next(MODEL_CONFIG, ID_FIELD)
add_related_objects(MODEL_CONFIG)
remove_fields(MODEL_CONFIG, DEFAULT_DELETE_FIELDS)
