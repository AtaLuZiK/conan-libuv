# conan-libuv

Conan package for [libuv](https://github.com/svaarala/libuv)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/libuv%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/libuv%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-libuv.svg?branch=release%2F1.24.0)](https://travis-ci.org/AtaLuZiK/conan-libuv)|[![Build status](https://ci.appveyor.com/api/projects/status/w5s9vfljc55yfnsw/branch/release/1.24.0?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-libuv/branch/release/1.24.0)|

## Reuse the packages

### Basic setup

```
conan install libuv/1.24.0@zimmerk/stable
```

### Project setup

```
[requires]
libuv/1.24.0@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
