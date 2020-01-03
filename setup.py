import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conveyor",
    version="0.0.1",
    license="MIT",
    author="Siddharth Garimella",
    author_email="sidgarimella@outlook.com",
    description="A toolset to accelerate Jupyter notebook workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidgarimella/conveyor",
    download_url="https://github.com/sidgarimella/conveyor/archive/v_001.tar.gz",
    packages=setuptools.find_packages(),
    install_requires=[
          'nbformat',
          'packaging'
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=2.7',
)
