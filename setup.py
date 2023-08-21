import setuptools
import os

readme = os.path.join(os.path.dirname(__file__), 'README.MD')
with open(readme, encoding='utf-8') as f:
    long_description = f.read()

version = '1.2.2'

setuptools.setup(
    name = "logandprint",
    version = version,
    author = "Guilherme Saldanha",
    author_email = "guisaldanha@gmail.com",
    description = "A simple logging package that helps you to log what is happening in your application.",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    license_files = ('LICENSE',),
    url = "https://github.com/guisaldanha/logandprint",
    packages=setuptools.find_packages(),
    project_urls={
        'Documentation': 'https://github.com/guisaldanha/logandprint/README.md',
        'Source': 'https://github.com/guisaldanha/logandprint',
        'Tracker': 'https://github.com/guisaldanha/logandprint/issues',
    },
    keywords=['python', 'log', 'logging', 'print', 'file'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    install_requires = []
)