from setuptools import setup, find_packages

setup(
    name="copyclipboard",  # This will be the name of your package on PyPI
    version="0.1.0",
    author="Amirarsalan Rajabi",
    description="A tool to copy folder structures and file contents to clipboard.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amirarsalan90/copyclipboard",  # Replace with your GitHub repo URL
    packages=find_packages(),
    py_modules=["main"],  # If your script is `main.py`
    entry_points={
        "console_scripts": [
            "copyclipboard=main:main",  # This will make `copyclipboard` executable from the command line
        ]
    },
    install_requires=[
        "pyperclip",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Adjust based on your package's compatibility
)
