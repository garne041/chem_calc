import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chem_calc", # Replace with your own username
    version="0.0.1",
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
    python_requires='>=3.2',
)
