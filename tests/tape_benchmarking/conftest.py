"""Test fixtures for TAPE datasets"""
import pytest
from dask.distributed import Client

from tape import Ensemble
from tape.utils import ColumnMapper


@pytest.fixture(scope="package", name="dask_client")
def dask_client():
    """Create a single client for use by all unit test cases."""
    client = Client()
    yield client
    client.close()


# pylint: disable=redefined-outer-name
@pytest.fixture
def s82_rrl_ensemble(dask_client):
    """Create an Ensemble from stripe 82 rrlyrae parquet data."""
    ens = Ensemble(client=dask_client)

    colmap = ColumnMapper(id_col="#id", time_col="mjd", flux_col="flux", err_col="error", band_col="band")
    ens.from_parquet(source_file="../../data/s82_rrlyrae/s82rrl_source.parquet",
                     object_file="../../data/s82_rrlyrae/s82rrl_object.parquet",
                     column_mapper=colmap,
                     provenance_label="sesar_2010")

    return ens


# pylint: disable=redefined-outer-name
@pytest.fixture
def s82_qso_ensemble(dask_client):
    """Create an Ensemble from stripe 82 QSO parquet data."""
    ens = Ensemble(client=dask_client)

    colmap = ColumnMapper(id_col="dbID", time_col="mjd", flux_col="flux", err_col="error", band_col="band")
    ens.from_parquet(source_file="../../data/s82_qso/s82qso_source.parquet",
                     object_file="../../data/s82_qso/s82qso_object.parquet",
                     column_mapper=colmap,
                     provenance_label="Southern Sample")

    return ens
