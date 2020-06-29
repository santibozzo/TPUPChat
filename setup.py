from setuptools import setup, find_packages

setup(
    name='Chat',
    version='0.1',
    packages=find_packages(),
    url='https://localhost:5000',
    # license='GPU',
    author='santibozzo',
    author_email='MyEmail@email.com',
    description='chat with flask',
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
