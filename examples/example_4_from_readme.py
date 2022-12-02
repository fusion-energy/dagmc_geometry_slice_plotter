from dagmc_geometry_slice_plotter import plot_slice

plot = plot_slice(
    dagmc_file_or_trimesh_object="dagmc.h5m",
    plane_normal=[1, 0, 0],
    plane_origin=[10, 0, 0],
    rotate_plot=270,
)

plot.savefig("example_4_slice.png")
