import os
import tarfile
import unittest
import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_file


class TestPlotSliceOfDagmcFile(unittest.TestCase):
    """Tests the neutronics utilities functionality and use cases"""

    def setUp(self):

        self.h5m_filename_smaller = "tests/dagmc.h5m"

    def test_create_default_plot(self):
        """Tests returned object is a matplotlib plot"""

        plot = plot_slice_of_dagmc_file(
            dagmc_filename=self.h5m_filename_smaller,
        )

        assert isinstance(plot, type(plt))

    def test_create_default_plot_file(self):
        """Tests output file creation"""

        os.system("rm test_plot.png")

        plot = plot_slice_of_dagmc_file(
            dagmc_filename=self.h5m_filename_smaller,
        )
        plot.savefig("test_plot.png")

        assert Path("test_plot.png").is_file()
