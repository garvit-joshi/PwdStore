import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PwdStore",
    version="0.1.3",
    author="Garvit Joshi",
    author_email="garvitjoshi9@gmail.com",
    description="A Package to store your Usernames, Password of a site in an encrypted file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garvit-joshi/PwdStore",
    packages=setuptools.find_packages(),
    keywords = "AES Crypt encrypt decrypt password",
    install_requires=['pyAesCrypt'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities',
    ],
    python_requires='>=3.4',
)
