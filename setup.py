from setuptools import setup, find_packages

setup(
    name='Chat',
    version='0.1',
    packages=find_packages(),
    url='https://localhost:8080',
    # license='GPU',
    author='Santiago Bozzo',
    author_email='MyEmail@email.com',
    description='chat with flask',
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
