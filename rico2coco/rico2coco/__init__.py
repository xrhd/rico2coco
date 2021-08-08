from rico2coco.coco_components import (
    get_annotations,
    get_categories,
    get_images,
    get_info,
    get_licenses,
)

__version__ = "0.1.0"


def run():
    return {
        "info": get_info(),
        "licenses": get_licenses(),
        "categories": list(get_categories()),
        "images": list(get_images()),
        "annotations": list(get_annotations()),
    }
