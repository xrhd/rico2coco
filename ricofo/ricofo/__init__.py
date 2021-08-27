import os

import fiftyone as fo
import fiftyone.zoo as foz

__version__ = "0.1.0"

IMAGES_DIR = "../rico2coco/rico/dataset/unique_uis/combined"
ANNOTATION_PATH = "../rico2coco/ricoco.json"


def main(image_dir: str = IMAGES_DIR, annotation_path: str = ANNOTATION_PATH):
    rico2coco_dataset = fo.Dataset.from_dir(
        dataset_type=fo.types.COCODetectionDataset,
        data_path=image_dir,
        labels_path=annotation_path,
        include_id=True,
        label_field="",
    )

    session = fo.launch_app(rico2coco_dataset)

    _quit = lambda: (input("Press q/Q to Quit")).lower() == "q"
    while _quit():
        pass
    else:
        print("Done!")


if __name__ == "__main__":
    main()
