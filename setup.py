from setuptools import setup
from codecs import open
from os import path

BASE = path.abspath(path.dirname(__file__))

with open(path.join(BASE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-multidomain',
    version='1.1.3',
    url='https://github.com/cyacarinic/django-multidomain',
    author='Claudio Yacarini',
    author_email='cyacarinic@gmail.com',
    description='Django application, set urls per domain.',
    packages=[
        'multidomain',
    ],
    install_requires=[
        'django-six'
    ],
    include_package_data=True,
    long_description = long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django url domain host multi',
)

