
A minimal Python package that produces slice plots through h5m DAGMC geometry files

# Installation

```bash
pip install dagmc_geometry_slice_plotter
```

# Python API Usage

These examples assume you have a h5m file called ```dagmc.h5m``` in the same folder that the Python script is being run from.

Create a plot of a slice through the geometry perpendicular to the Z axis and 
default settings elsewhere. This will slice through the the center of the
geometry as plane_origin has not been specified.

```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_file

plot = plot_slice_of_dagmc_file(
    dagmc_filename='dagmc.h5m',
    plane_normal = [0, 0, 1],
)

plot.show()
```

Create a plot of a slice through the geometry perpendicular to the Z axis, offset by 20cm and with default settings elsewhere.
```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_file

plot = plot_slice_of_dagmc_file(
    dagmc_filename='dagmc.h5m',
    plane_origin= 20,
    plane_normal = [0, 0, 1],
)

plot.show()
```

Create a plot of a slice through the geometry perpendicular to the Y axis, with a rotation of 90 degrees and with default settings elsewhere.
```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_file

plot = plot_slice_of_dagmc_file(
    dagmc_filename='dagmc.h5m',
    plane_normal = [0, 1, 0],
    rotate_plot=90
)

plot.show()
```

Saves a png image of a plot of a slice through the geometry perpendicular to the X axis and with default settings elsewhere.
```python
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_file

plot = plot_slice_of_dagmc_file(
    dagmc_filename='dagmc.h5m',
    plane_normal = [1, 0, 0],
    output_filename='my_plot.png'
)
```