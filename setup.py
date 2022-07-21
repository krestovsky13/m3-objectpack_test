from setuptools import setup, find_packages

setup(name='m3-objectpack-test',
      version='1.0',
      url='https://github.com/krestovsky13/m3-objectpack_test',
      author='Nikita Krestyannikov',
      packages=find_packages(),
      install_requires=[
          'Django==2.2',
          'pip==22.1.2',
          'pytz==2022.1',
          'setuptools==60.2.0',
          'six==1.16.0',
          'sqlparse==0.4.2',
          'wheel==0.37.1',
          'm3-builder==1.2.0',
          'm3-core==2.2.24',
          'm3-django-compat==1.9.2',
          'm3-objectpack==2.2.47',
          'm3-ui==2.2.105',
      ],
      include_package_data=True,
      zip_safe=False,
      dependency_links=['https://pypi.bars-open.ru/packages/m3-django-compat-1.9.2.tar.gz',
                        'https://pypi.bars-open.ru/packages/m3-builder-1.2.0.tar.gz'],
      # entry_points={
      #     'console_scripts':
      #         []
      # }
      )
