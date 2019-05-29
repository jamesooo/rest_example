import setuptools

setuptools.setup(
    name = 'rest_example-jamesooo',
    version = '0.3',
    author = "James O'Neal",
    description = 'An exapmle of a python rest api',
    url = 'https://github.com/jamesooo/rest_example',
    packages = setuptools.find_packages(),
    install_requires = [
        'Flask-RESTful==0.3.7',
        'Click==7.0'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)
