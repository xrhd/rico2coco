import os

import fiftyone as fo
import fiftyone.zoo as foz


__version__ = '0.1.0'

IMAGES_DIR = "../rico2coco/rico/dataset/unique_uis/combined"
ANNOTATION_PATH = "../rico2coco/ricoco.json"

rico2coco_dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=IMAGES_DIR,
    labels_path=ANNOTATION_PATH,
    include_id=True,
    label_field="",
)

session = fo.launch_app(rico2coco_dataset)
