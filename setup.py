from setuptools import setup


# Reads the content of your README.md into a variable to be used in the setup below
def get_long_description() -> str:
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name='azurapy',  # should match the package folder
    packages=['azurapy'],  # should match the package folder
    version='0.0.2',  # important for updates
    license='MIT',  # should match your chosen license
    description='Simple python API integration for AzuraCast',
    long_description=get_long_description(),  # loads your README.md
    long_description_content_type='text/markdown',  # README.md is of type 'markdown'
    author='Artem `artctv`',
    author_email='artctvcode@gmail.com',
    url='https://github.com/artctv/azurapy',
    download_url='https://github.com/artctv/azurapy/archive/refs/tags/v0.0.2.tar.gz',
    # project_urls={  # Optional
    #     "Bug Tracker": ""
    # },
    install_requires=['httpx>=0.22.0'],  # list all packages that your package uses
    keywords=['pypi', 'azurapy'],  # descriptive meta-data
    classifiers=[  # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
