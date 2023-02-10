# this example makes use of the dagmc_geometry_slice_ploter to extract the
# dagmc geometry outline.

from dagmc_geometry_slice_plotter import get_slice_coordinates
import matplotlib.pyplot as plt

data = get_slice_coordinates(
    dagmc_file_or_trimesh_object="dagmc.h5m",
    plane_origin=[0, 0, 200],
    plane_normal=[0, 0, 1],
)

plt.axes().set_aspect("equal")

for xy in data:
    plt.plot(*xy, color="black", linewidth=1)

plt.savefig("example_7_slice.png")
