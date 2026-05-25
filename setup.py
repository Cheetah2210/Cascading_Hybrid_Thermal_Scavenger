from setuptools import setup, find_packages

setup(
    name="chts_physics",
    version="0.3.0",
    description="Cascading Hybrid Thermal Scavenger Physics Engine",
    author="Emily 🌻 (Cheetahs Creations)",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26.0",
        "pytest>=8.0.0",
    ],
    python_requires=">=3.11",
)
