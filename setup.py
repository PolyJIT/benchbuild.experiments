from setuptools import setup, find_namespace_packages

with open('README.md') as f:
    long_description = f.read()

setup(name='benchbuild.experiments',
      use_scm_version=True,
      url='https://github.com/PolyJIT/benchbuild.experiments',
      packages=find_namespace_packages(include=['benchbuild.experiments']),
      setup_requires=["pytest-runner", "setuptools_scm"],
      tests_require=["pytest"],
      install_requires=[
          "benchbuild>4.0.1",
      ],
      author="Andreas Simbuerger",
      author_email="simbuerg@fim.uni-passau.de",
      description=
      "Experiments curated for the benchbuild empirical research toolkit.",
      long_description=long_description,
      long_description_content_type='text/markdown',
      license="MIT",
      classifiers=[
          'Development Status :: 4 - Beta', 'Intended Audience :: Developers',
          'Topic :: Software Development :: Testing',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      keywords="benchbuild experiments run-time")
