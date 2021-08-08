import json

import numpy as np
import pandas as pd

from rico2coco.config import COMPRESSION_FACTOR, RICO_DATASET_PATH
from rico2coco.metadata import rico_metadata
from rico2coco.utils import get_components_from_view_hierarchy


def get_info():
    return {
        "year": "2021",
        "version": "1.0",
        "description": "Custum Rico Dataset in Coco format.",
        "contributor": "xrhd",
        "url": "",
        "date_created": "",
    }


def get_licenses():
    return [{}]


def get_categories(component_legend: pd.DataFrame = rico_metadata.component_legend):
    for i, label_name in enumerate(component_legend):
        yield {"supercategory": "none", "id": i + 1, "name": label_name}


def get_images(ui_details: pd.DataFrame = rico_metadata.ui_detail):
    width, height = 1080, 1920  # img.size
    for ui_id in ui_details["UI Number"]:
        yield {
            "id": int(ui_id) + 1,
            "height": height,
            "width": width,
            "file_name": f"{ui_id}.jpg",
        }


def get_annotations(
    rico_dataset_path: str = RICO_DATASET_PATH,
    ui_details: pd.DataFrame = rico_metadata.ui_detail,
    categories_map: dict = {obj["name"]: obj["id"] for obj in get_categories()},
):
    print(categories_map)

    anotatiin_id = 0

    for ui_id in ui_details["UI Number"]:
        view_hierarchy_file_path = f"{rico_dataset_path}/{ui_id}.json"
        view_hierarchy = json.load(open(view_hierarchy_file_path))
        components = get_components_from_view_hierarchy(view_hierarchy)

        for component_label, bounds in components:
            if component_label in categories_map and component_label != "background":
                anotatiin_id += 1
                x0, y0, x1, y1 = list(np.array(bounds) * COMPRESSION_FACTOR)
                area = (y1 - y0) * (x1 - x0)
                bbox = (x0, y0, x1 - x0, y1 - y0)

                yield {
                    "id": anotatiin_id,
                    "image_id": int(ui_id) + 1,
                    "category_id": categories_map.get(component_label, 0),
                    "bbox": bbox,
                    "area": area,
                    "iscrowd": 0,
                    "ignore": 1 if area <= 0 else 0,
                    "segmentation": [],
                }
