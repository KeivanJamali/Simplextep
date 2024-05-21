import setuptools

setuptools.setup(
    name="Simplextep",
    version=0.26,
    author="Keivan Jamali",
    author_email="K1Jamali01@gmail.com",
    description="Solving Simplex with showing all steps and analyse it.",
    packages=setuptools.find_packages(),
    install_requires=["numpy", "pandas", "tabulate", "matplotlib"],
    license="MIT",
)