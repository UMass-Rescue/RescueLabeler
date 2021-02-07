from setuptools import setup

setup(
    name="rescue_labeler_api",
    version="0.1.0",
    url="https://github.com/UMass-Rescue/RescueLabeler",
    author="Jagath Jai Kumar",
    description="API for internal text labeling",
    packages=["labeler_api"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["fastapi", "python-multipart", "uvicorn"],
)
