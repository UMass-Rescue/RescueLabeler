from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="rescue_labeler_api",
    version="0.1.0",
    url="https://github.com/UMass-Rescue/RescueLabeler",
    author="Jagath Jai Kumar",
    description="API for internal text labeling",
    packages=["app"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=required,
)
