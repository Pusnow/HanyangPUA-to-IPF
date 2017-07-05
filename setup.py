from setuptools import setup
import hpuaipk

setup(
    name='hpuaipk',
    version=hpuaipk.__version__,
    description='A simple Hanyang PUA to IPK converter',
    long_description=open("README.rst", "r", encoding="utf8").read(),
    license='MIT',
    author='Wonsup Yoon',
    maintainer='Wonsup Yoon',
    maintainer_email='pusnow@me.com',
    packages=['hpuaipk'],
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console'],
    entry_points={
        'console_scripts': ['hpuaipk = hpuaipk:main'],
    }, )
