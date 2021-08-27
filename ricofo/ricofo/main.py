import fiftyone as fo
import fiftyone.zoo as foz

from ricofo.config import *


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
