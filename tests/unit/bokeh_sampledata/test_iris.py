# -----------------------------------------------------------------------------
# Copyright (c) Bokeh Contributors
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
from __future__ import annotations

import pandas as pd

import bokeh_sampledata.iris as m

ALL = ("flowers",)


def test___all__() -> None:
    assert m.__all__ == ALL


def test_flowers() -> None:
    assert isinstance(m.flowers, pd.DataFrame)

    assert len(m.flowers) == 150
