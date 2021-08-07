import pandas as pd

from rico2coco.config import COMPONENT_LEGEND_FILENAME, UI_DETAILS_FILENAME


class RicoMetadata:
    def __init__(self, ui_detail_filename, componet_legend_filename) -> None:
        self.ui_detail = pd.read_csv(ui_detail_filename, header=0)
        self.component_legend = pd.read_json(componet_legend_filename)


rico_metadata = RicoMetadata(UI_DETAILS_FILENAME, COMPONENT_LEGEND_FILENAME)
