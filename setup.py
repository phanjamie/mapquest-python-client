from setuptools import setup, find_packages

setup(
    name='mapquest-python',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'requests'
    ]
)