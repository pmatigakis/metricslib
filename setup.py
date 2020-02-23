from setuptools import setup, find_packages


def get_requirements(requirements_file):
    with open(requirements_file) as f:
        return [
            line.strip()
            for line in f
            if not line.startswith(("-e", "#", "\n"))
        ]


setup(
    name="metricslib",
    version="0.1.0",
    description="Metrics collection library",
    author="Panagiotis Matigakis",
    author_email="pmatigakis@gmail.com",
    packages=find_packages(exclude=["tests"]),
    zip_safe=True,
    install_requires=get_requirements("requirements.txt"),
    test_suite='nose.collector',
    tests_require=get_requirements("requirements-test.txt"),
)
