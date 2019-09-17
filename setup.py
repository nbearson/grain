from setuptools import setup, find_packages

setup(name='grain',
      version='1.0.2019-09',
      description='A super simple UTC<->TAI conversion package',
      author='Nick Bearson',
      author_email='nickb@ssec.wisc.edu',
      license='GPLv3',
      packages=find_packages('.'),
      install_requires=[],
      include_package_data = True,
      package_data = { 'grain' : ['leap-seconds.list'] },
      )

