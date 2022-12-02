from dagmc_geometry_slice_plotter import plot_axis_slice

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object="dagmc.h5m",
    plane_origin=[0, 0, 200],
    view_direction="z",
)

plot.savefig("example_2_slice.png")
