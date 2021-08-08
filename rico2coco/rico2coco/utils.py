def get_components_from_view_hierarchy(view_hierarchy):
    components = []

    def _get_componets(componet):
        if not componet:
            return

        if "bounds" in componet:
            components.append(
                (componet.get("componentLabel", "background"), componet.get("bounds"))
            )

        for children_componet in componet.get("children", []):
            _get_componets(children_componet)

    _get_componets(view_hierarchy)
    return components
