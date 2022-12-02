from pathlib import Path
from typing import Optional, Tuple, Union

import matplotlib.pyplot as plt
import trimesh
from matplotlib import transforms


def plot_axis_slice(
    dagmc_file_or_trimesh_object: Union[str, trimesh.Trimesh, trimesh.Scene],
    view_direction: str,
    plane_origin: Tuple[float, float, float] = None,
):
    """Axis aligned plane normal slices through a 3D DAGMC geometry file
    (h5m format) and produces a matplotlib plot of the slice.

    Args:
        dagmc_file_or_trimesh_object: the filename of the DAGMC h5m file or a
            A trimesh mesh object. This can be created from a DAGMC h5m file in
            the following way 'trimesh_mesh_object = trimesh.load_mesh(
            dagmc_filename, process=False)'.
        view_direction: the axis to view the geometry from. Acceptable options
            are '-z', 'z', '-x', 'x', '-y', 'y' (just like Paraview)
        plane_origin: the origin of the plain, if None then the centroid of
            the mesh will be used.

    Return:
        A matplotlib.pyplot object
    """

    acceptable_values = ["-z", "z", "-x", "x", "-y", "y"]
    if view_direction not in acceptable_values:
        raise ValueError(
            f"view_direction must be one of the following {acceptable_values}"
        )

    if view_direction == "-z":
        plane_normal = [0, 0, -1]
        rotate_plot = 0
    if view_direction == "z":
        plane_normal = [0, 0, 1]
        rotate_plot = 0
    if view_direction == "-y":
        plane_normal = [0, -1, 0]
        rotate_plot = 90
    if view_direction == "y":
        plane_normal = [0, 1, 0]
        rotate_plot = 90
    if view_direction == "-x":
        plane_normal = [-1, 0, 0]
        rotate_plot = -90
    if view_direction == "x":
        plane_normal = [1, 0, 0]
        rotate_plot = 90

    slice = plot_slice(
        dagmc_file_or_trimesh_object=dagmc_file_or_trimesh_object,
        plane_origin=plane_origin,
        plane_normal=plane_normal,
        rotate_plot=rotate_plot,
    )

    return slice


def plot_slice(
    dagmc_file_or_trimesh_object: Union[str, trimesh.Trimesh, trimesh.Scene],
    plane_origin: Tuple[float, float, float] = None,
    plane_normal: Union[Tuple[float, float, float], str] = [0, 0, 1],
    rotate_plot: float = 0,
):
    """Arbitrary plane normal slices through a 3D DAGMC geometry file
    (h5m format) and produces a matplotlib plot of the slice.

    Args:
        dagmc_file_or_trimesh_object: the filename of the DAGMC h5m file or a
            A trimesh mesh object. This can be created from a DAGMC h5m file in
            the following way 'trimesh_mesh_object = trimesh.load_mesh(
            dagmc_filename, process=False)'.
        plane_origin: the origin of the plain, if None then the centroid of
            the mesh will be used.
        plane_normal: the plane to slice the geometry on. Defaults to slicing
            along the Z plane which is input as [0, 0, 1].
        rotate_plot: the angle in degrees to rotate the plot by. Useful when
            used in conjunction with changing plane_normal to orientate the
            plot correctly.

    Return:
        A matplotlib.pyplot object
    """

    if isinstance(dagmc_file_or_trimesh_object, str):
        slice = plot_slice_of_dagmc_file(
            dagmc_filename=dagmc_file_or_trimesh_object,
            plane_origin=plane_origin,
            plane_normal=plane_normal,
            rotate_plot=rotate_plot,
        )

    else:

        slice = plot_slice_of_trimesh_object(
            trimesh_mesh_object=dagmc_file_or_trimesh_object,
            plane_origin=plane_origin,
            plane_normal=plane_normal,
            rotate_plot=rotate_plot,
        )

    return slice


def plot_slice_of_dagmc_file(
    dagmc_filename: str,
    plane_origin: Tuple[float, float, float] = None,
    plane_normal: Tuple[float, float, float] = [0, 0, 1],
    rotate_plot: float = 0,
) -> plt:
    """Slices through a 3D DAGMC geometry file (h5m format) and produces a
    matplotlib plot of the slice.

    Args:
        dagmc_filename: the filename of the DAGMC h5m file.
        plane_origin: the origin of the plain, if None then the centroid of
            the mesh will be used.
        plane_normal: the plane to slice the geometry on. Defaults to slicing
            along the Z plane which is input as [0, 0, 1].
        rotate_plot: the angle in degrees to rotate the plot by. Useful when
            used in conjunction with changing plane_normal to orientate the
            plot correctly.

    Return:
        A matplotlib.pyplot object
    """

    if not Path(dagmc_filename).is_file():
        raise FileNotFoundError(f"file {dagmc_filename} not found.")

    trimesh_mesh_object = trimesh.load_mesh(dagmc_filename, process=False)

    plot = plot_slice_of_trimesh_object(
        trimesh_mesh_object=trimesh_mesh_object,
        plane_origin=plane_origin,
        plane_normal=plane_normal,
        rotate_plot=rotate_plot,
    )

    return plot


def plot_slice_of_trimesh_object(
    trimesh_mesh_object: Union[trimesh.Trimesh, trimesh.Scene],
    plane_origin: Tuple[float, float, float] = None,
    plane_normal: Tuple[float, float, float] = [0, 0, 1],
    rotate_plot: float = 0,
) -> plt:
    """Slices through a trimesh_mesh_object and produces a matplotlib plot of
    the slice. Accepts a trimesh_mesh_object which avoids reloading the mesh
    file each time a new plot is required.

    Args:
        trimesh_mesh_object: A trimesh mesh object. This can be created from a
            DAGMC h5m file in the following way 'trimesh_mesh_object =
            trimesh.load_mesh(dagmc_filename, process=False)'
        plane_origin: the origin of the plain, if None then the centroid of
            the mesh will be used.
        plane_normal: the plane to slice the geometry on. Defaults to slicing
            along the Z plane which is input as [0, 0, 1].
        rotate_plot: the angle in degrees to rotate the plot by. Useful when
            used in conjunction with changing plane_normal to orientate the
            plot correctly.

    Return:
        A matplotlib.pyplot object
    """

    if plane_origin is None:
        plane_origin = trimesh_mesh_object.centroid
    slice = trimesh_mesh_object.section(
        plane_origin=plane_origin,
        plane_normal=plane_normal,
    )

    if slice is None:
        msg = (
            "The geometry slice returned None which means no geometry was "
            "intersected, try changing the plane_origin or plane_normal"
        )
        raise ValueError(msg)

    to_2D = trimesh.geometry.align_vectors(plane_normal, [0, 0, -1])

    slice_2D, to_3D = slice.to_planar(to_2D=to_2D)

    plt.close()

    # keep plot axis scaled the same
    plt.axes().set_aspect("equal")  # an option to increase box size "datalim"

    if rotate_plot != 0:
        base = plt.gca().transData
        rot = transforms.Affine2D().rotate_deg(rotate_plot)

    for entity in slice_2D.entities:

        discrete = entity.discrete(slice_2D.vertices)

        if rotate_plot != 0:
            plt.plot(*discrete.T, color="black", linewidth=1, transform=rot + base)
        else:
            plt.plot(*discrete.T, color="black", linewidth=1)

    return plt
