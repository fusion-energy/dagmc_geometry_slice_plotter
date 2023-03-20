import streamlit as st
from dagmc_geometry_slice_plotter import plot_axis_slice


def save_uploadedfile(uploadedfile):
    with open(uploadedfile.name, "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success(f"Saved File to {uploadedfile.name}")


def header():
    """This section writes out the page header common to all tabs"""

    st.set_page_config(
        page_title="DAGMC slice plot",
        page_icon="⚛",
        layout="wide",
    )

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {
                    visibility: hidden;
                    }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.write(
        """
            # DAGMC geometry slice plotter

            ### ⚛ A plotting user interface for slicing DAGMC geometry.

            🐍 Run this app locally with Python ```pip install dagmc_geometry_slice_plotter``` then run with ```dagmc_geometry_slice_plotter```

            ⚙ Produce MatPlotLib plots in batch with the 🐍 [Python API](https://github.com/fusion-energy/dagmc_geometry_slice_plotter/tree/master/examples)

            💾 Raise a feature request, report and issue or make a contribution on [GitHub](https://github.com/fusion-energy/dagmc_geometry_slice_plotter)

            📧 Email feedback to mail@jshimwell.com

            🔗 This package forms part of a more [comprehensive openmc plot](https://github.com/fusion-energy/openmc_plot) package where geometry, tallies, slices, etc can be plotted and is hosted on [xsplot.com](https://www.xsplot.com/) .
        """
    )

    st.write("<br>", unsafe_allow_html=True)


def main():
    st.write(
        """
            👉 Create your ```dagmc.h5m``` file using one of the methods listed in on the [DAGMC tools discussion](https://github.com/svalinn/DAGMC/discussions/812):

        """
    )

    dagmc_h5m_file = st.file_uploader("Upload your dagmc.h5m file", type=["h5m"])

    if dagmc_h5m_file == None:
        new_title = '<p style="font-family:sans-serif; color:Red; font-size: 30px;">Upload your geometry.xml</p>'
        st.markdown(new_title, unsafe_allow_html=True)

        st.write(
            """
                Not got a DAGMC h5m file handy, right mouse 🖱️ click and save these links 
                [ example 1 ](https://fusion-energy.github.io/openmc_geometry_plot/examples/dagmc_tokamak/dagmc_180_tokamak.h5m)
            """
        )

    else:
        save_uploadedfile(dagmc_h5m_file)

        try:
            # only used to find bounding box, could replace with
            # https://github.com/fusion-energy/dagmc_bounding_box
            import openmc
        except:
            msg = "import openmc failed, please make sure openmc is installed"
            st.write(msg)
            raise ValueError(msg)

        dagunv = openmc.DAGMCUniverse(dagmc_h5m_file.name).bounded_universe()
        bb = dagunv.bounding_box

        view_direction = st.sidebar.selectbox(
            label="View Direction", options=("-z", "z", "-x", "x", "-y", "y"), index=0
        )

        if view_direction in ["-x", "x"]:
            x_offset = st.sidebar.slider(
                label="X axis offset",
                min_value=float(bb[0][0]),
                max_value=float(bb[1][0]),
                value=float((bb[0][0] + bb[1][0]) / 2),
            )
        else:
            x_offset = float((bb[0][0] + bb[1][0]) / 2)

        if view_direction in ["-y", "y"]:
            y_offset = st.sidebar.slider(
                label="Y axis offset",
                min_value=float(bb[0][1]),
                max_value=float(bb[1][1]),
                value=float((bb[0][1] + bb[1][1]) / 2),
            )
        else:
            y_offset = float((bb[0][1] + bb[1][1]) / 2)

        if view_direction in ["-z", "z"]:
            z_offset = st.sidebar.slider(
                label="Z axis offset",
                min_value=float(bb[0][2]),
                max_value=float(bb[1][2]),
                value=float((bb[0][2] + bb[1][2]) / 2),
            )
        else:
            z_offset = float((bb[0][2] + bb[1][2]) / 2)

        dag_plt = plot_axis_slice(
            dagmc_file_or_trimesh_object=dagmc_h5m_file.name,
            view_direction=view_direction,
            plane_origin=[x_offset, y_offset, z_offset],
        )
        st.pyplot(dag_plt)

        dag_plt.savefig("openmc_plot_dagmc_slice_image.png")

        with open("openmc_plot_dagmc_slice_image.png", "rb") as file:
            st.sidebar.download_button(
                label="Download image",
                data=file,
                file_name="openmc_plot_dagmc_slice_image.png",
                mime="image/png",
            )


if __name__ == "__main__":
    header()
    main()
