from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="PyAero",
    version="2.1.8",
    description="PyAero is an open-source airfoil contour analysis and CFD meshing tool written in Python.",
    author="chiefenne",
    author_email="chiefenne@nowhere.com",
    license="MIT",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
