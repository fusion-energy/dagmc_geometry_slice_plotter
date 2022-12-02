from importlib.metadata import version

__version__ = version("dagmc_geometry_slice_plotter")

__all__ = ["__version__"]

from .utils import plot_slice_of_dagmc_file
from .utils import plot_slice_of_trimesh_object
from .utils import plot_slice
from .utils import plot_axis_slice
