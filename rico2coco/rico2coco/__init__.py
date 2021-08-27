from rico2coco.coco_components import (
    get_annotations,
    get_categories,
    get_images,
    get_info,
    get_licenses,
)

__version__ = "0.1.0"


def run(label_key: str = "componentLabel"):
    dataset = {
        "info": get_info(),
        "licenses": get_licenses(),
        "categories": list(get_categories(label_key=label_key)),
        "images": list(get_images()),
    }

    categories_map = {obj["name"]: obj["id"] for obj in dataset["categories"]}
    dataset["annotations"] = list(
        get_annotations(label_key=label_key, categories_map=categories_map)
    )

    return dataset
