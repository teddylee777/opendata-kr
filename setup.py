from setuptools import setup, find_packages

setup(
    name='opendata-kr',
    version='0.0.3',
    description='Sample Datasets for Beginners',
    author='Teddy Lee',
    author_email='teddylee777@gmail.com',
    url='https://github.com/teddylee777/opendata-kr',
    install_requires=['tqdm', 'pandas', 'ipywidgets', 'requests'],
    packages=find_packages(exclude=[]),
    keywords=['opendata-kr', 'opendata', 'teddynote', 'datasets', 'sample-datasets', 'python', 'pandas', 'sample', 'data'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
