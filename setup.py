from setuptools import setup, find_packages


def get_requirements(requirements_file):
    with open(requirements_file) as f:
        return [
            line.strip()
            for line in f
            if not line.startswith(("-e", "#", "\n"))
        ]


with open("README.md") as f:
    long_description = f.read()


setup(
    name="metricslib",
    version="0.3.0",
    description="Metrics collection library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Panagiotis Matigakis",
    author_email="pmatigakis@gmail.com",
    url="https://github.com/pmatigakis/metricslib",
    packages=find_packages(exclude=["tests"]),
    zip_safe=True,
    install_requires=get_requirements("requirements.txt"),
    test_suite='nose.collector',
    tests_require=get_requirements("requirements-test.txt"),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires='>=3.5'
)
