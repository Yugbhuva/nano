from setuptools import setup, find_packages

setup(
    name='nanourls',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Yug Bhuva',
    description='A tiny Python URL shortener',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
