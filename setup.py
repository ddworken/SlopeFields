from distutils.core import setup

setup(
    name='SlopeFields',
    version='0.1.0',
    author='David Dworken',
    author_email='david@daviddworken.com',
    packages=['SlopeFields'],
    url='http://pypi.python.org/pypi/SlopeFields/',
    license='LICENSE.txt',
    description='A Slope Field generator and grapher. ',
    long_description=open('README.rst').read(),
    scripts=['SlopeFields/SlopeFields.py'],
    install_requires=[
        "argparse",
        "matplotlib",
        "numpy",
    ],
)
