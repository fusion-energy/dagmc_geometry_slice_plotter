[![N|Python](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://www.python.org)

[![CI with install](https://github.com/fusion-energy/dagmc_geometry_slice_plotter/actions/workflows/ci_with_install.yml/badge.svg?branch=develop)](https://github.com/fusion-energy/dagmc_geometry_slice_plotter/actions/workflows/ci_with_install.yml)

[![PyPI](https://img.shields.io/pypi/v/dagmc-geometry-slice-plotter?color=brightgreen&label=pypi&logo=grebrightgreenen&logoColor=green)](https://pypi.org/project/dagmc-geometry-slice-plotter/)

<!-- [![codecov](https://codecov.io/gh/fusion-energy/dagmc_geometry_slice_plotter/branch/main/graph/badge.svg)](https://codecov.io/gh/fusion-energy/dagmc_geometry_slice_plotter) -->

A minimal Python package that produces slice plots through h5m DAGMC geometry files

# Installation

```bash
pip install dagmc_geometry_slice_plotter
```

# Python API Usage

These examples assume you have a h5m file called ```dagmc.h5m``` in the same
folder that the Python script is being run from.

Create a plot of a slice through the geometry perpendicular to the Z axis and
default settings elsewhere. This will slice through the the center of the
geometry as plane_origin has not been specified.

```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_geometry

plot = plot_slice_of_dagmc_geometry(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_normal=[0, 0, 1],
)

plot.show()
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321345-9187aa57-c3bc-4940-ae28-1237df394eba.png)

Create a plot of a slice through the geometry perpendicular to the Z axis,
offset by 200cm and with default settings elsewhere.
```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_geometry

plot = plot_slice_of_dagmc_geometry(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_origin=[0, 0, 200],
    plane_normal=[0, 0, 1],
)

plot.show()
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321353-707bf553-1255-4a87-a3b9-d97aa3ecb67b.png)

Create a plot of a slice through the geometry perpendicular to the Y axis, with
a rotation of 45 degrees and with default settings elsewhere. Also saves the
plot with a high resolution (DPI)
```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_geometry

plot = plot_slice_of_dagmc_geometry(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_normal=[0, 1, 0],
    rotate_plot=45,
)

plot.savefig('my_plot3.png', dpi=600)
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321358-194162d4-8d42-4090-811e-0dd3768a328d.png)

Saves a png image of a plot of a slice through the geometry perpendicular to
the X axis and with default settings elsewhere.
```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_geometry

plot_slice_of_dagmc_geometry(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_normal = [1, 0, 0],
    rotate_plot=270,
    output_filename='my_plot4.png'
)
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321363-0e7604b3-74eb-44e8-8aa2-9586c008b40d.png)


# Related packages

This package is used by the [regular_mesh_plotter](https://github.com/fusion-energy/regular_mesh_plotter) Python package to combine slice plots with regular mesh tally results and produce images like below.

![paramak plot openmc regular mesh tally](https://user-images.githubusercontent.com/8583900/138322007-daf1eb6f-ca42-4d9c-9581-8dbc9da94fe5.png)

![paramak plot openmc regular mesh tally](https://user-images.githubusercontent.com/8583900/138322010-c7ca7ced-1a37-4af5-b7a4-7d5853a2b9bb.png)
