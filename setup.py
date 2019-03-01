from setuptools import setup, find_packages

setup(name='grain',
      version='1.0.2019-01',
      description='A super simple UTC<->TAI conversion package',
      author='Nick Bearson',
      author_email='nickb@ssec.wisc.edu',
      packages=find_packages('.'),
      install_requires=[],
      include_package_data = True,
      package_data = { 'grain' : ['leap-seconds.list'] },
      )

