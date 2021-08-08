from rico2coco.coco_transformer import (
    get_annotations,
    get_images,
    get_info,
    get_licenses,
)


def test_get_inf():
    assert isinstance(get_info(), dict)


def test_get_licenses():
    assert isinstance(get_licenses(), list)


def test_get_images():
    image_data = next(get_images())
    assert isinstance(image_data, dict)
    for attribute in ["id", "height", "width", "file_name"]:
        assert attribute in image_data


def test_get_annotations():
    annotations = next(get_annotations())
    assert isinstance(annotations, dict)
    for attribute in ["id", "image_id", "category_id", "bbox", "area"]:
        assert attribute in annotations
