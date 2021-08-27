import os

import fiftyone as fo
import fiftyone.zoo as foz

__version__ = "0.1.0"

IMAGES_DIR = "../rico2coco/rico/dataset/unique_uis/combined"
ANNOTATION_PATH = "../rico2coco/ricoco.json"
MAX_SAMPLES = 100


def main(
    image_dir: str = IMAGES_DIR,
    annotation_path: str = ANNOTATION_PATH,
    max_samples: int = MAX_SAMPLES,
):
    rico2coco_dataset = fo.Dataset.from_dir(
        dataset_type=fo.types.COCODetectionDataset,
        data_path=image_dir,
        labels_path=annotation_path,
        include_id=True,
        label_field="",
        max_samples=max_samples,
    )

    session = fo.launch_app(rico2coco_dataset)
    session.wait()


if __name__ == "__main__":
    main()
