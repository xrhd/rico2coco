import json

import pandas as pd

from rico2coco.config import RICO_DATASET_PATH
from rico2coco.metadata import rico_metadata
from rico2coco.utils import decompose_bounds, get_components_from_view_hierarchy


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


def get_categories(
    label_key: str = "componentLabel",
):
    if label_key == "clickable":
        legends = ["clickable", "not_clickable"]

    elif label_key == "iconClass":
        legends = rico_metadata.icon_legend

    else:
        legends = rico_metadata.component_legend

    for i, label_name in enumerate(legends):
        yield {"supercategory": "none", "id": i + 1, "name": label_name}


def get_images(ui_details: pd.DataFrame = rico_metadata.ui_detail, valid_data_set=None):
    image_id = 0
    width, height = 1080, 1920  # img.size

    for ui_id in ui_details["UI Number"]:
        if ui_id in valid_data_set:
            image_id += 1
            yield {
                "id": image_id,
                "height": height,
                "width": width,
                "file_name": f"{ui_id}.jpg",
            }


def get_annotations(
    coco_images,
    rico_dataset_path: str = RICO_DATASET_PATH,
    categories_map: dict = {obj["name"]: obj["id"] for obj in get_categories()},
    label_key: str = "componentLabel",
):
    anotatiin_id = 0

    for coco_image in coco_images:
        ui_id = coco_image["file_name"].split(".").pop(0)
        view_hierarchy_file_path = f"{rico_dataset_path}/{ui_id}.json"
        view_hierarchy = json.load(open(view_hierarchy_file_path))
        components = get_components_from_view_hierarchy(view_hierarchy, label_key)

        for component_label, bounds in components:
            if component_label in categories_map and component_label != "background":
                anotatiin_id += 1
                bbox, area = decompose_bounds(bounds)

                yield {
                    "id": anotatiin_id,
                    "image_id": coco_image["id"],
                    "category_id": categories_map.get(component_label, 0),
                    "bbox": bbox,
                    "area": area,
                    "iscrowd": 0,
                    "ignore": 1 if area <= 0 else 0,
                    "segmentation": [],
                }
