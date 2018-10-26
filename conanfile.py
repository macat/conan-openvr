from conans import ConanFile, CMake, tools


class OpenvrConan(ConanFile):
    name = "openvr"
    version = "1.0.17"
    description = ("API and runtime that allows access to VR hardware from"
                   "multiple vendors without requiring that "
                   "applications have specific knowledge of the hardware they"
                   "are targeting.")
    url = "https://github.com/ArsenStudio/conan-{0}".format(name)
    homepage = "https://github.com/ValveSoftware/openvr"
    license = "BSD 3-Clause"

    exports = ["LICENSE.md"]

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    build_subfolder = "build_subfolder"
    branch = ("v" if version != "master" else "") + version

    def source(self):
        git = tools.Git(folder="openvr")
        git.clone("https://github.com/ValveSoftware/openvr.git", "master")
        git.checkout(self.branch)
        tools.replace_in_file("openvr/CMakeLists.txt", "project(OpenVRSDK)",
                              '''project(OpenVRSDK)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="openvr")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="cobs-c")
        self.copy("*cobs.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
