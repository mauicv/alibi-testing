import os
from setuptools import setup, find_packages


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


# load all data files recursively https://stackoverflow.com/a/36693250
model_files = package_files('alibi_testing/models/')

setup(
    name='alibi-testing',
    version='0.0.11',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[  # deps version bounds are copied from alibi setup.py (and requirements/dev.txt)
        'numpy>=1.16.2, <2.0.0',
        'pandas>=0.23.3, <2.0.0',
        'requests>=2.21.0, <3.0.0',
        'scikit-learn>=0.20.2, <2.0.0',
        'tensorflow>=2.0.0, !=2.6.0, !=2.6.1, <2.10.0',  
        'torch>=1.9.0, <2.0.0',
        'torchvision>=0.10.0, <1.0.0'
    ],
    package_data={'': model_files}
)
