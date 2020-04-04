import setuptools

#with open("README.md", "r") as fh:
    #long_description = fh.read()


setuptools.setup(
    name="currentclidate",
    version="1.0.0",
    author="balakrishna Soura",
    email="soura_balakrishna49@yahoo.com",
    description="A small example package",
    long_description="long_description",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
