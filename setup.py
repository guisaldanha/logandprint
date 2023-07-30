import setuptools

version = '1.1'

setuptools.setup(
    name = "logandprint",
    version = version,
    author = "Guilherme Saldanha",
    author_email = "guisaldanha@gmail.com",
    description = "A simple logging package that helps you to log what is happening in your application.",
    long_description = "This logging package is a straightforward yet powerful tool that assists developers in logging the activities occurring within their application. It provides a user-friendly interface and customizable settings, enabling developers to generate comprehensive logs that document events and actions within their application. This package is an essential tool for developers who want to troubleshoot issues, improve performance, and optimize the user experience",
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