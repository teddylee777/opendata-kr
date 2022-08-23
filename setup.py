from setuptools import setup, find_packages

setup(
    name='opendata-kr',
    version='0.0.1',
    description='Sample Datasets for Beginners',
    author='Teddy Lee',
    author_email='teddylee777@gmail.com',
    url='https://github.com/teddylee777/opendata-kr',
    install_requires=['tqdm', 'pandas', 'jupyter', 'ipywidgets', 'requests'],
    packages=find_packages(exclude=[]),
    keywords=['teddynote', 'datasets', 'sample-datasets', 'python', 'pandas', 'sample', 'data'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
