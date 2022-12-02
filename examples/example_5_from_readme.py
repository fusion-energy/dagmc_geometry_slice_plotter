from dagmc_geometry_slice_plotter import plot_slice


def make_slice_plot(x_height):
    """A minimal function that takes the slice height"""

    plot = plot_slice(
        dagmc_file_or_trimesh_object="dagmc.h5m",
        plane_normal=[0, 0, 1],
        plane_origin=[0, 0, x_height],
        rotate_plot=90,
    )

    plot.savefig(f"example_5_slice_{str(x_height).zfill(3)}.png")


for x in range(0, 500, 20):
    make_slice_plot(x_height=x)
