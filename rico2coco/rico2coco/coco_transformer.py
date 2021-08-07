import pandas as pd

from rico2coco.metadata import rico_metadata


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


def get_annotations(semantic_annotation: dict):
    pass
