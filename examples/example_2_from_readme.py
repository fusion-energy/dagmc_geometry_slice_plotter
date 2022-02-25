
from dagmc_geometry_slice_plotter import plot_slice_of_dagmc_geometry

plot = plot_slice_of_dagmc_geometry(
    dagmc_file_or_trimesh_object='dagmc.h5m',
    plane_origin=[0, 0, 200],
    plane_normal=[0, 0, 1],
)

plot.savefig('example_2_slice.png')