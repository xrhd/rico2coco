from rico2coco.coco_components import *

__version__ = "0.1.0"


def run():
    return {
        "info": get_info(),
        "licenses": get_licenses(),
        "categories": get_categories(),
        "images": get_images(),
        "annotations": get_annotations(),
    }
