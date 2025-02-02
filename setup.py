from setuptools import find_packages, setup

setup(
    name="aklp",
    # packages=find_packages(),
	packages=find_packages(where="src"),
    package_dir={"": "src"},
    version='0.0.2',
    description="Python library to deserialize Arknights' story data",
    author="Meph1sto666",
	install_requires=[],
	setup_requires=['pytest-runner'],
	tests_require=['pytest>=7.0'],
	test_suite='tests',
	python_requires=">=3.10.6"
)