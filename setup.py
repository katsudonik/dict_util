import setuptools
 
setuptools.setup(
    name="dict_util",
    version="1.4.2",
    license='MIT',
    install_requires=['numpy', 'pandas'],
    author="katsudonik",
    author_email="kaikeda.work@gmail.com",
    description="python dict utility package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords='dict, df, dict to df, df to dict, compare dict',
    url="https://github.com/katsudonik/dict_util",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
