import os
import tarfile
import unittest
import urllib.request
from pathlib import Path
import trimesh

import matplotlib.pyplot as plt
from dagmc_geometry_slice_plotter import plot_slice_of_trimesh_object


class TestPlotSliceOfTrimeshObject(unittest.TestCase):
    """Tests the neutronics utilities functionality and use cases"""

    def setUp(self):

        if not Path("tests/v0.0.2.tar.gz").is_file():
            url = "https://github.com/fusion-energy/neutronics_workflow/archive/refs/tags/v0.0.2.tar.gz"
            urllib.request.urlretrieve(url, "tests/v0.0.2.tar.gz")

            tar = tarfile.open("tests/v0.0.2.tar.gz", "r:gz")
            tar.extractall("tests")
            tar.close()

        h5m_filename_smaller = "tests/neutronics_workflow-0.0.2/example_01_single_volume_cell_tally/stage_2_output/dagmc.h5m"
        h5m_filename_bigger = "tests/neutronics_workflow-0.0.2/example_02_multi_volume_cell_tally/stage_2_output/dagmc.h5m"

        self.trimesh_mesh_object_smaller = trimesh.load_mesh(h5m_filename_smaller, process=False)
        self.trimesh_mesh_object_bigger = trimesh.load_mesh(h5m_filename_bigger, process=False)

    def test_create_default_plot(self):
        """Tests returned object is a matplotlib plot"""

        plot = plot_slice_of_trimesh_object(
            trimesh_mesh_object=self.trimesh_mesh_object_smaller,
        )

        assert isinstance(plot, type(plt))

        plot2 = plot_slice_of_trimesh_object(
            trimesh_mesh_object=self.trimesh_mesh_object_bigger,
        )

        assert isinstance(plot2, type(plt))

    def test_create_default_plot_file(self):
        """Tests output file creation"""

        os.system("rm test_plot.png")

        plot_slice_of_trimesh_object(
            trimesh_mesh_object=self.trimesh_mesh_object_smaller,
            output_filename="test_plot.png",
        )

        assert Path("test_plot.png").is_file()

        os.system("rm test_plot2.png")

        plot_slice_of_trimesh_object(
            trimesh_mesh_object=self.trimesh_mesh_object_bigger,
            output_filename="test_plot2.png",
        )

        assert Path("test_plot2.png").is_file()
