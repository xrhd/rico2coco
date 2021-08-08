import pandas as pd

from rico2coco.metadata import rico_metadata


def test_rico_metadata():
    assert isinstance(rico_metadata.ui_detail, pd.DataFrame)
    assert isinstance(rico_metadata.component_legend, pd.DataFrame)
