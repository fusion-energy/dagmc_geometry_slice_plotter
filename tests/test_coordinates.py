import os
import unittest
from pathlib import Path

import matplotlib.pyplot as plt
from dagmc_geometry_slice_plotter import get_slice_coordinates


class TestPlotSliceOfDagmcFile(unittest.TestCase):
    """Tests the neutronics utilities functionality and use cases"""

    def setUp(self):
        self.h5m_filename_smaller = "tests/dagmc.h5m"

    def test_create_default_plot(self):
        """Tests returned object is a matplotlib plot"""

        list_of_coords = get_slice_coordinates(
            dagmc_file_or_trimesh_object=self.h5m_filename_smaller,
        )

        for xy in list_of_coords:
            plt.plot(*xy, color="black", linewidth=1)

        assert isinstance(list_of_coords, list)

    def test_create_default_plot_file(self):
        """Tests output file creation"""

        os.system("rm test_plot.png")

        list_of_coords = get_slice_coordinates(
            dagmc_file_or_trimesh_object=self.h5m_filename_smaller,
        )

        for xy in list_of_coords:
            plt.plot(*xy, color="black", linewidth=1)

        assert isinstance(list_of_coords, list)
        # TODO consider making the function return lists of floats not a TrackedArray
