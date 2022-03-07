try:
    from importlib.metadata import version, PackageNotFoundError
except (ModuleNotFoundError, ImportError):
    from importlib_metadata import version, PackageNotFoundError
try:
    __version__ = version("dagmc_geometry_slice_plotter")
except PackageNotFoundError:
    from setuptools_scm import get_version

    __version__ = get_version(root="..", relative_to=__file__)

__all__ = ["__version__"]

from .utils import plot_slice_of_dagmc_file
from .utils import plot_slice_of_trimesh_object
from .utils import plot_slice_of_dagmc_geometry
