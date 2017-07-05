from setuptools import setup
import hpuaipf

setup(
    name='hpuaipf',
    version=hpuaipf.__version__,
    description='A simple Hanyang PUA to IPF converter',
    long_description=open("README.rst", "r", encoding="utf8").read(),
    license='MIT',
    author='Wonsup Yoon',
    maintainer='Wonsup Yoon',
    maintainer_email='pusnow@me.com',
    packages=['hpuaipf'],
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console'],
    entry_points={
        'console_scripts': ['hpuaipf = hpuaipf:main'],
    }, )
