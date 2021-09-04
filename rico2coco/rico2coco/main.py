from rico2coco.coco_components import (
    get_annotations,
    get_categories,
    get_images,
    get_info,
    get_licenses,
)
from rico2coco.config import LABEL_KEY, RICO_SCA_FITER_FILE


def run(label_key: str = LABEL_KEY, filer_file: str = RICO_SCA_FITER_FILE):

    valid_data_set = None
    if filer_file:
        valid_data_set = set()
        with open(filer_file) as filter_file:
            for line in filter_file:
                ui_id = int(line.strip().split(".").pop(0))
                valid_data_set.add(ui_id)

    dataset = {
        "info": get_info(),
        "licenses": get_licenses(),
        "categories": list(get_categories(label_key=label_key)),
        "images": list(get_images(valid_data_set=valid_data_set)),
    }

    categories_map = {obj["name"]: obj["id"] for obj in dataset["categories"]}
    print(categories_map)

    dataset["annotations"] = list(
        get_annotations(
            coco_images=dataset["images"],
            label_key=label_key,
            categories_map=categories_map,
        )
    )
    return dataset
