[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?maxAge=3600)](https://raw.githubusercontent.com/mmha/conan-google-benchmark/master/LICENSE)
[![Travis CI](https://img.shields.io/travis/mmha/conan-google-benchmark/master.svg?label=Travis%20CI)](https://travis-ci.org/mmha/conan-google-benchmark)
[![AppVeyor](https://img.shields.io/appveyor/ci/mmha/conan-google-benchmark/master.svg?label=AppVeyor)](https://ci.appveyor.com/project/mmha/conan-google-benchmark)
[![Download](https://api.bintray.com/packages/mmha/public-conan/google-benchmark%3Ammha/images/download.svg)](https://bintray.com/mmha/public-conan/google-benchmark%3Ammha/_latestVersion)

# conan-google-benchmark

[Conan](https://bintray.com/mmha/public-conan) package for [Google Benchmark](https://github.com/google/benchmark) library.

The package generated with this **conanfile** can be found at [mmha/public-conan](https://bintray.com/mmha/public-conan/google-benchmark%3Ammha).

`conan` client can be downloaded from [Conan.io](https://conan.io).

## Reuse the package

### Add public-conan remote

To add [mmha/public-conan](https://bintray.com/mmha/public-conan) remote to your
local `conan` instance run:

```bash
conan remote add mmha https://api.bintray.com/conan/mmha/public-conan
```

### Basic setup

```
$ conan install google-benchmark/1.5.0@mmha/stable --build=missing
```

### Project setup

If you handle multiple dependencies in your project, it would be better
to add a `conanfile.txt`

```
[requires]
google-benchmark/1.5.0@mmha/stable

[options]

[generators]
cmake_paths
```

or if you are using `conanfile.py` file add:

```python
requires = "google-benchmark/1.5.0@mmha/stable"
```

Complete the installation of requirements for your project running:

```
mkdir build
cd build
conan install .. --build=outdated <your_profile_and_settings>
<your typical build process>
```

Project setup installs the library (and all its dependencies), and assuming you chose
`cmake_paths` as a generator, it generates `conan_paths.cmake` file that defines variables
to make CMake `find_package()` work and find all the dependencies in the Conan local cache.


## Build package

```
$ conan create . <user>/<channel> <your_profile_and_settings>
```

## Upload package to server

```
$ conan upload -r <remote-name> --all google-benchmark/1.5.0@<user>/<channel>
```
