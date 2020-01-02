import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conveyor",
    version="0.0.1",
    author="Siddharth Garimella",
    author_email="sidgarimella@outlook.com",
    description="A toolset to accelerate Jupyter notebook workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/jupyter-conveyor",
    packages=setuptools.find_packages(),
    install_requires=[
          'nbformat'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
