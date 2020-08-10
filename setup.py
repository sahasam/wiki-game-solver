from distutils.core import setup
from setuptools import find_packages

setup(
    name='wikigamesolver',
    version='1.0.0',
    author='Sahas Munamala',
    author_email='munamalasahas@gmail.com',
    packages=find_packages(),
    url='https://github.com/sahasam/wiki=game-solver',
    license='MIT License',
    descrption='Find the shortest path between any two wikipedia links',
    long_description='Find the shortest path between any two wikipedia links',
    zip_safe=False,
    entry_points={"console_scripts": ["wikigamesolver=wikigamesolver.__main__:main"]}
)