"""Test TAPE-readability of datasets"""

import pytest


@pytest.mark.parametrize(
    "data_fixture",
    [
        "s82_rrl_ensemble",
        "s82_qso_ensemble",
    ],
)
def test_from_parquet(data_fixture, request):
    """
    Test that ensemble loader functions successfully load parquet files
    """
    parquet_ensemble = request.getfixturevalue(data_fixture)

    assert parquet_ensemble._source is not None
    assert parquet_ensemble._object is not None
