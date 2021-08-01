from setuptools import setup

packages = ["rico2coco"]

package_data = {"": ["*"]}

setup_kwargs = {
    "name": "rico2coco",
    "version": "0.1.0",
    "description": "",
    "long_description": None,
    "author": "xrhd",
    "author_email": "rhd@icomp.ufam.edu.br",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "python_requires": ">=3.8,<4.0",
}


setup(**setup_kwargs)
