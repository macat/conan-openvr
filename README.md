# Conan package of OpenVR
[![Download](https://api.bintray.com/packages/arsen-studio/arsen-deps/openvr%3Aarsen-studio/images/download.svg)](https://bintray.com/arsen-studio/arsen-deps/openvr%3Aarsen-studio/_latestVersion)

|Linux|Windows|OS X|
|-----|-------|----|
|[![pipeline status](https://gitlab.com/HeiGameStudio/ArsenEngine/dependencies/conan-openvr/badges/master/pipeline.svg)](https://gitlab.com/HeiGameStudio/ArsenEngine/dependencies/conan-openvr/commits/master)|[![Build status](https://ci.appveyor.com/api/projects/status/ab587jq8fdv8xmiw/branch/master?svg=true)](https://ci.appveyor.com/project/intelligide/conan-openvr/branch/master)|[![Build Status](https://travis-ci.org/ArsenStudio/conan-openvr.svg?branch=master)](https://travis-ci.org/ArsenStudio/conan-openvr)|

[Conan.io](https://conan.io) package for [OpenVR](https://github.com/ValveSoftware/openvr) SDK.

The packages generated with this **conanfile** can be found in [bintray.com](https://bintray.com/arsen-studio/arsen-deps/openvr%3Aarsen-studio).

## Setup
To configure Conan client to work with Arsen packages, you will need to add repository to the list of remotes. To add repository, use the following command: 
```
conan remote add arsen-deps https://api.bintray.com/conan/arsen-studio/arsen-deps 
```

### Basic

```
$ conan install openvr/latest@arsen-studio/stable
```

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

```
[requires]
openvr/latest@arsen-studio/stable

[options]
openvr:shared=true # false

[generators]
txt
cmake
```

Complete the installation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

## Develop the package

### Build packages

    $ pip install conan_package_tools bincrafters_package_tools
    $ python build.py

### Upload packages to server

    $ conan upload openvr/latest@arsen-studio/stable --all

## Issues

If you wish to report an issue, please do so here:

https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-openvr/issues

For any pull or merge request, please do so here:

https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-openvr/merge_requests


## License

[MIT LICENSE](LICENSE)