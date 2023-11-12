from setuptools import find_packages, setup

setup(
    name="picpaychallenge",
    version="0.0.1",
    description="TBD",
    author_email="munhozarthur@gmail.com",
    license="MIT",
    packages=find_packages(exclude=["contrib", "docs"]),
    extras_require={},
    include_package_data=True,
    entry_points={},
    install_requires=[
        "email-validator==2.1.0.post1",
        "pydantic==2.4.2",
        "pytz==2023.3.post1",
        "SQLAlchemy==2.0.23",
        "python-dotenv==1.0.0",
    ],
)
