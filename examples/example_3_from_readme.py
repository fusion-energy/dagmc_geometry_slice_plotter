from dagmc_geometry_slice_plotter import plot_slice

plot = plot_slice(
    dagmc_file_or_trimesh_object="dagmc.h5m",
    plane_normal=[0, 1, 0],
    rotate_plot=45,
)

plot.savefig("example_3_slice.png", dpi=600)
