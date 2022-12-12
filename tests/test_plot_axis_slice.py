import os
import tarfile
import unittest
import urllib.request
from pathlib import Path
import trimesh

import matplotlib.pyplot as plt
from dagmc_geometry_slice_plotter import plot_axis_slice


class TestPlotSliceOfTrimeshObject(unittest.TestCase):
    """Tests the neutronics utilities functionality and use cases"""

    def setUp(self):

        h5m_filename_smaller = "tests/dagmc.h5m"

        self.trimesh_mesh_object_smaller = trimesh.load_mesh(
            h5m_filename_smaller, process=False
        )

    def test_create_default_plot(self):
        """Tests returned object is a matplotlib plot"""

        plot = plot_axis_slice(
            view_direction="x",
            dagmc_file_or_trimesh_object=self.trimesh_mesh_object_smaller,
        )

        assert isinstance(plot, type(plt))

    def test_create_default_plot_file(self):
        """Tests output file creation"""

        os.system("rm test_plot.png")

        plot = plot_axis_slice(
            view_direction="y",
            dagmc_file_or_trimesh_object=self.trimesh_mesh_object_smaller,
        )
        plot.savefig("test_plot.png")

        assert Path("test_plot.png").is_file()
