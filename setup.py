import setuptools

setuptools.setup(
    author="Beth Cimini",
    author_email="bcimini@broadinstitute.org",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    extras_require={
        "dev": [
            "black==19.10b0",
            "click>=7.1.2",
            "pre-commit==2.2.0",
            "sphinx==3.1.2",
            "twine==3.1.1",
        ],
        "test": ["pytest==5.4.1"],
    },
    install_requires=[
        "centrosome==1.2.0",
        "mahotas>=1.4",
        "matplotlib==3.1.3",
        "mysqlclient==1.4.6",
        "numpy>=1.20.1",
        "scikit-image>=0.17.2",
        "scikit-learn>=0.20",
        "scipy>=1.4.1",
    ],
    license="BSD",
    name="cellprofiler-library",
    package_data={"cellprofiler-library": ["py.typed", "napari.yaml"]},
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.8",
    url="https://github.com/CellProfiler/library",
    version="0.0.0",
    zip_safe=False,
    entry_points={
        "napari.manifest": ["cellprofiler_library=cellprofiler_library:napari.yaml",],
        "napari.plugin": ["cellprofiler_library = cellprofiler_library._function",],
    }
)