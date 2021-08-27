import numpy as np

from rico2coco.config import COMPRESSION_FACTOR


def get_componentLabel(component):
    return component.get("componentLabel", "background")


def get_clickable(component):
    is_clickable = component.get("clickable", "background")
    if is_clickable:
        return "clickable"
    return "not_clickable"


LABEL_KEYS_EXTRACTOR = {
    "componentLabel": get_componentLabel,
    "clickable": get_clickable,
}


def get_components_from_view_hierarchy(view_hierarchy, label_key="componentLabel"):
    if label_key not in LABEL_KEYS_EXTRACTOR:
        raise Exception(f"label_key {label_key} not supported!")

    label_extractor = LABEL_KEYS_EXTRACTOR[label_key]
    components = []

    def _get_components(component):
        if not component:
            return

        if "bounds" in component:
            components.append((label_extractor(component), component.get("bounds")))

        for children_component in component.get("children", []):
            _get_components(children_component)

    _get_components(view_hierarchy)
    return components


def decompose_bounds(bounds, compression_factor=COMPRESSION_FACTOR):
    x0, y0, x1, y1 = list(np.array(bounds) * compression_factor)
    area = (y1 - y0) * (x1 - x0)
    bbox = (x0, y0, x1 - x0, y1 - y0)
    return bbox, area
