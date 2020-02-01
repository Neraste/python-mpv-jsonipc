from setuptools import setup
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-mpv-jsonipc',
    version='1.0.0',
    author="Ian Walton",
    author_email="iwalton3@gmail.com",
    description="Python API to MPV using JSON IPC",
    license='GPLv3',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iwalton3/python-mpv-jsonipc",
    packages=['python_mpv_jsonipc'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)