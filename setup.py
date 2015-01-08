from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='testapp',
    version=version,
    description='Test App',
    author='Web Notes',
    author_email='pdvyas@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
