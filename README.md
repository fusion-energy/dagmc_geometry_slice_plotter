[![N|Python](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://www.python.org)

[![CI with install](https://github.com/fusion-energy/dagmc_geometry_slice_plotter/actions/workflows/ci_with_install.yml/badge.svg?branch=develop)](https://github.com/fusion-energy/dagmc_geometry_slice_plotter/actions/workflows/ci_with_install.yml)

[![PyPI](https://img.shields.io/pypi/v/dagmc-geometry-slice-plotter?color=brightgreen&label=pypi&logo=grebrightgreenen&logoColor=green)](https://pypi.org/project/dagmc-geometry-slice-plotter/)

[![codecov](https://codecov.io/gh/fusion-energy/dagmc_geometry_slice_plotter/branch/main/graph/badge.svg?token=Dm3sNp4q8X)](https://codecov.io/gh/fusion-energy/dagmc_geometry_slice_plotter)

A minimal Python package that produces slice plots through h5m DAGMC geometry files

# Installation

```bash
pip install dagmc_geometry_slice_plotter
```

# Python API Usage

These examples assume you have a h5m file called ```dagmc.h5m``` in the same
folder that the Python script is being run from.

The ```plot_axis_slice``` method allows simple axis aligned plots to be made
with minimal user effort.

Create a plot of a slice through the geometry perpendicular to the Z axis and
default settings elsewhere. This will slice through the the center of the
geometry as ```plane_origin``` has not been specified in this example.

```python
from dagmc_geometry_slice_plotter import plot_axis_slice

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    view_direction='z',
)

plot.show()
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321345-9187aa57-c3bc-4940-ae28-1237df394eba.png)

Create a plot of a slice through the geometry perpendicular to the Z axis,
offset by 200cm and with default settings elsewhere.
```python
from dagmc_geometry_slice_plotter import plot_axis_slice

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_origin=[0, 0, 200],
    view_direction='z'
)

plot.show()
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321353-707bf553-1255-4a87-a3b9-d97aa3ecb67b.png)

The ```plot_slice``` function allows more control over the plot as it allows
arbitrary plane normals so that off axis slices can be made and allows the plot
to be rotated.

Create a plot of a slice through the geometry perpendicular to the Y axis, with
a rotation of 45 degrees and with default settings elsewhere. Also saves the
plot with a high resolution (DPI)
```python
from dagmc_geometry_slice_plotter import plot_slice

plot = plot_slice(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_normal=[0, 1, 0],
    rotate_plot=45,
)

plot.savefig('example_3_slice.png', dpi=600)
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321358-194162d4-8d42-4090-811e-0dd3768a328d.png)

Saves a png image of a plot of a slice through the geometry perpendicular to
the X axis and and with an offset in the x axis.
```python
from dagmc_geometry_slice_plotter import plot_slice

plot = plot_slice(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_normal = [1, 0, 0],
    plane_origin=[10, 0, 0],
    rotate_plot=270,
)

plot.savefig('example_4_slice.png')
```
![dagmc slice plot](https://user-images.githubusercontent.com/8583900/138321363-0e7604b3-74eb-44e8-8aa2-9586c008b40d.png)

DAGMC files can also be made using packages like [cad_to_dagmc](https://github.com/fusion-energy/cad_to_dagmc) or [stl_to_h5m](https://github.com/fusion-energy/stl_to_h5m). This example uses CadQuery to make an STL file then converts the STL file to a DAGMC h5m file and plots a slice through the geometry  

# Custom plots

You can also use the package to access the the coordinates and lines that make
up the outline and then plot these lines with your own MatplotLib script or
other plotting package.

This example makes use of low level functionality in the package to extract the
coordinates and lines then plot them in MatPlotLib. This offers users full
customization of how the plots appear and also allows the plots to be combined
with other types of plots such as 

```python
from dagmc_geometry_slice_plotter import get_slice_coordinates
import matplotlib.pyplot as plt

data = get_slice_coordinates(
    dagmc_file_or_trimesh_object="dagmc.h5m",
    plane_origin=[0, 0, 200],
    plane_normal=[0, 0, 1],
)

plt.axes().set_aspect("equal")  # scales the x y axis 1:1

for xy in data:
    plt.plot(*xy, color="black", linewidth=1)

plt.savefig("example_7_slice.png")
```

# Related packages

- This package is used by the [openmc_plot](https://github.com/fusion-energy/openmc_plot) Python package which has a web deployed version at [xsplot.com](http://www.xsplot.com)


- This package can also be used together with the [openmc_geometry_plot](https://github.com/fusion-energy/openmc_geometry_plot) Python package to combine outline slice plots of DAGMC geometry with colored areas for materials or cells

- This package can also be used together with the [regular_mesh_plotter](https://github.com/fusion-energy/regular_mesh_plotter) Python package to combine outline
slice plots with regular mesh tally results and produce images like below.

![paramak plot openmc regular mesh tally](https://user-images.githubusercontent.com/8583900/138322007-daf1eb6f-ca42-4d9c-9581-8dbc9da94fe5.png)

![paramak plot openmc regular mesh tally](https://user-images.githubusercontent.com/8583900/138322010-c7ca7ced-1a37-4af5-b7a4-7d5853a2b9bb.png)
