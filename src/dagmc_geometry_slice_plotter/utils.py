def view_direction_to_plane_normal(view_direction):
    convertor_dict = {
        "-z": [0, 0, -1],
        "z": [0, 0, 1],
        "-y": [0, -1, 0],
        "y": [0, 1, 0],
        "-x": [-1, 0, 0],
        "x": [1, 0, 0],
    }
    return convertor_dict[view_direction]


def view_direction_to_rotate_plot(view_direction):
    convertor_dict = {
        "-z": 0,
        "z": 0,
        "-y": 90,
        "y": 90,
        "-x": -90,
        "x": 90,
    }
    return convertor_dict[view_direction]


def view_direction_to_x_y_label(view_direction):
    convertor_dict = {
        "-z": ("X [cm]", "Y [cm]"),
        "z": ("X [cm]", "Y [cm]"),
        "-y": ("X [cm]", "Z [cm]"),
        "y": ("X [cm]", "Z [cm]"),
        "-x": ("Y [cm]", "Z [cm]"),
        "x": ("Y [cm]", "Z [cm]"),
    }
    return convertor_dict[view_direction]
