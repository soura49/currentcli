import setuptools

#with open("README.md", "r") as fh:
    #long_description = fh.read()


setuptools.setup(
    name="currentcli",
    version="1.0.0",
    author="balakrishna Soura",
    email="soura_balakrishna49@yahoo.com",
    description="A small example package",
    long_description="long_description",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': [
            'currentcli = currentcli.__main__:main'
        ]
    }
)
