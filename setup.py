from setuptools import setup, find_packages

setup(
    name='myPackage',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    description="EDSA Example Python Package",
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<Jackam-spec>/<myPackage>',
    author='<Jack Kamire>',
    author_email='jacmire@gmail.com'
)
