import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="complexnumbers",
    version="0.0.2",
    author="DLS",
    author_email="author@example.com",
    description="A small example package for complex numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=['nose>=1.3.7',
                      'numpy==1.15.2',
                      'packaging==18.0',
                      'pyparsing==2.2.2',
                      'scipy==1.1.0',
                      'six>=1.11.0',
                      'sparsegrad==0.0.10'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
