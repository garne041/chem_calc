import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="chem_calc", # Replace with your own username
    version="0.0.3",
    author="Joy Garnett",
    author_email="garne041@gmail.com",
    description="A package to calculate various stoichometric features of compounds.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garne041/chem_calc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires = ['numpy', 'pandas'],
    setup_requires = ['numpy', 'pandas'],
    python_requires='>=3.2',
)
