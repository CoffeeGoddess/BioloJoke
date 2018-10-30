import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BioloJoke",
    version="0.5.0",
    author="CoffeeGoddess",
    author_email="contactspaceboom@gmail.com",
    description="Science comedy, cause you can't be geek enough.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoffeeGoddess/BioloJoke",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Natural Language :: English',
    ],
    include_package_data=True
)
