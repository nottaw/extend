import setuptools


setuptools.setup(
    name = "extend",
    version = "0.1",
    py_modules = ["extend"],
    install_requires = ["click", "filetype"],
    entry_points = """
        [console_scripts]
        extend=extend:extend
    """
)
