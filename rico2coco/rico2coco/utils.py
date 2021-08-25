from io import DEFAULT_BUFFER_SIZE


def get_componentLabel(component):
    return component.get("componentLabel", "background")


def get_clickable(component):
    is_clickable = component.get("componentLabel", "background").lower()
    if is_clickable == "true":
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
