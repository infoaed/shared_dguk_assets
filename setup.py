try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from ckan import (__version__, __description__, __long_description__,
                  __license__)

setup(
    name='ckan',
    version=__version__,
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    license=__license__,
    url='http://ckan.org/',
    description=__description__,
    packages=['ckan-i18n-js'],
    keywords='data packaging component tool server',
    long_description=__long_description__,
    message_extractors={
        'src/js': [
            ('**.js', 'javascript', None),
        ],
        'i18n-ext/ckanext-dgu': [
            ('ckanext/dgu/theme/templates/viz/**', 'ignore', None),
            ('node_modules/**', 'ignore', None),
            ('**.js', 'javascript', None),
        ],
        'i18n-ext/ckanext-harvest': [
            ('**.js', 'javascript', None),
        ],
        'i18n-ext/ckanext-ga-report': [
            ('**.js', 'javascript', None),
        ],
        'i18n-ext/ckanext-spatial': [
            ('**.js', 'javascript', None),
        ],
    }
)
