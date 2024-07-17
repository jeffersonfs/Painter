# Ultralytics pip template

import pathlib
from pathlib import Path

from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent.resolve()  # current path
long_description = (here / "README.md").read_text(
    encoding="utf-8"
)  # Get the long description from the README file
with open(
    here / "src/SegGPT_inference/requirements.txt"
) as fp:  # read requirements.txt
    install_reqs = [r.rstrip() for r in fp.readlines() if not r.startswith("#")]

setup(
    name="SegGPT-inference",
    version="0.0.0",
    description="Pip project SegGPT.",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Jefferson F. Silva",
    author_email="jefferson.fs@ufma.br",
    url="https://github.com/jeffersonfs/Painter",
    project_urls={
        "Bug Reports": "https://github.com/jeffersonfs/Painter/issues",
        "Source": "https://github.com/jeffersonfs/Painter",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    setup_requires=[],
    install_requires=[],
    python_requires=">=3.8, <4",
)
