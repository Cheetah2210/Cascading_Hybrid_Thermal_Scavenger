from setuptools import setup, find_packages

setup(
    name="chts_physics_engine",
    version="3.0.0",
    author="Emily (Cheetahs Creations)",
    description="Core simulation and physics validation engines for the Cascading Hybrid Thermal Scavenger",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "matplotlib>=3.7.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: CERN Open Hardware Licence v1.2",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
