from setuptools import setup, find_namespace_packages

setup(
    name="Clean folder",
    version="0.0.1",
    description="This script sorts your folder",
    author="Bogdan Kataryna",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": [
        "clean-folder=clean_folder.clean:main"]
    }
)
