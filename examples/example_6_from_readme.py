# demonstrates the geometry view from different view directions

import cadquery as cq
from cadquery import exporters
from stl_to_h5m import stl_to_h5m
from dagmc_geometry_slice_plotter import plot_slice, plot_axis_slice
import os


def create_text_h5m(text):
    text = cq.Workplane("XY").text(txt=text, fontsize=5, distance=2)
    exporters.export(text, "text.stl")
    stl_to_h5m(
        files_with_tags=[("text.stl", "mat1")],
        h5m_filename="dagmc_text.h5m",
    )


os.system("mbconvert dagmc_text.h5m dagmc_text.vtk")

create_text_h5m("DAGMC geometry slice plotter")

plot = plot_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m", plane_normal=[0, 0, -1]
)
plot.title("-z")
plot.show()

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m", view_direction="-z"
)
plot.show()


plot = plot_slice(dagmc_file_or_trimesh_object="dagmc_text.h5m", plane_normal=[0, 0, 1])
plot.title("z")
plot.show()

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m", view_direction="z"
)
plot.show()


plot = plot_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m",
    plane_normal=[0, -1, 0],
    rotate_plot=90,
)
plot.title("-y")
plot.show()

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m", view_direction="-y"
)
plot.show()


plot = plot_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m",
    plane_normal=[0, 1, 0],
    rotate_plot=90,
)
plot.title("y")
plot.show()

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m", view_direction="y"
)
plot.show()


plot = plot_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m",
    plane_normal=[-1, 0, 0],
    rotate_plot=-90,
)
plot.title("-x")
plot.show()

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m", view_direction="-x"
)
plot.show()


plot = plot_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m",
    plane_normal=[1, 0, 0],
    rotate_plot=90,
)
plot.title("x")
plot.show()

plot = plot_axis_slice(
    dagmc_file_or_trimesh_object="dagmc_text.h5m", view_direction="x"
)
plot.show()
