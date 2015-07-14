from setuptools import setup, find_packages

setup(
		name='ripcast',
		version='0.0.1',
		author="Charlie Hack",
		author_email="charles.t.hack@gmail.com",
		description="automatic podcasts.",
		packages=find_packages(),
		include_package_data=True,
		install_requires=[
                        'soundcloud',
		]
)

