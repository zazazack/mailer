import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f:
    long_description = '\n' + f.read()


about = {}

with open(os.path.join(here, 'mailer', '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name='mailer',
    author='Zachary Wilson',
    author_email='zwilson.development@gmail.com',
    description='Configurable mass email command line interface.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests", "tests.*", "tasks", "tasks.*"]),
    version=about['__version__'],
    license='GNUv3',
    url='https://github.com/zazazack/mailer')
