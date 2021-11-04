import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dagmc_geometry_slice_plotter",
    version="develop",
    author="The Regular Mesh Plotter Development Team",
    author_email="mail@jshimwell.com",
    description="A minimal Python package for creating plots of slices through DAGMC geometry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fusion-energy/dagmc_geometry_slice_plotter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_data={
        "dagmc_geometry_slice_plotter": [
            # "requirements.txt",
            "README.md",
            "LICENSE",
        ]
    },
    install_requires=[
        "matplotlib>=3.4.2",
        "trimesh",
        "shapely",
        "scipy",
        "meshio",  # required to allow trimesh to read h5m files
        "h5py",
    ],
)
