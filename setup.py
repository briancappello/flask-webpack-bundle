from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Flask Webpack Bundle',
    version='0.1.0',
    description='Adds Webpack support to Flask Unchained',
    long_description=long_description,
    url='https://github.com/briancappello/flask-webpack-bundle',
    author='Brian Cappello',
    license='GPLv3',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'flask-unchained>=0.2.0',
        'MarkupSafe>=1.0',
    ],
    include_package_data=True,
    zip_safe=False,
)
