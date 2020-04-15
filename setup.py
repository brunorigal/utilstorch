import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='utils_torch',  
     version='0.1',
     author="Bruno Rigal",
     author_email="",
     description="A package for training torch NN",
     long_description=long_description,
    long_description_content_type="text/markdown",
     url="https://github.com/brunorigal/utils_torch.git",
    #  packages=setuptools.find_packages(),
        packages=['utils_torch'],  #same as name
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
 )
