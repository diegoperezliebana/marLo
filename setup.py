from setuptools import setup, find_packages

setup(name='marlo',
      version='0.0.1dev14',
      description='Marlo',
      url='https://github.com/crowdAI/marlo',
      author='S.P. Mohanty',
      author_email='sharada.mohanty@epfl.ch',
      license='MIT License',
      packages=find_packages(),
      package_data = {
        '':['envs/*/templates/*.xml']
      },
      zip_safe=False,
      install_requires=['gym', 'jinja2'],
      dependency_links=[]
)
