from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="gmapFinder",
	version="1.0.1",
	license='MIT',
	author="Roshan Kumar",
	author_email="roshanthakur8571@gmail.com",
	description="Gives the direction on Google Maps",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/roshan9419/gmapFinder",
	packages=setuptools.find_packages(),
	keywords=["getDirection", "getDistance", "getCurrentLocation"],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	include_package_data=True,
	install_requires=["geopy","requests"],
)