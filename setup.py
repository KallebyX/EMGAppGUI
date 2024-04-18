# setup.py
from setuptools import setup, find_packages

setup(
    name="EMGApp",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'PyQt5', 'numpy', 'matplotlib', 'scipy', 'pyserial', 'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'emgapp = src.main:main',
        ],
    },
    python_requires='>=3.6',
)
