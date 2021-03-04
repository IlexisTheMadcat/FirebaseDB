import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="FirebaseDB-dict",
    version="0.5.0",
    description="Live interaction to a Firebase Realtime Database.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SUPERMECHM500/FirebaseDB",
    author="MECH HUB FACTORY",
    author_email="thedestoryer11@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.5",
    ],
    packages=["FirebaseDB"],
    include_package_data=True,
    install_requires=["firebase_admin"],
    }
)
