from conans import ConanFile, CMake, tools


class OpenvrConan(ConanFile):
    """
    OpenVR is an API and runtime that allows access to VR hardware from multiple vendors without 
    requiring that applications have specific knowledge of the hardware they are targeting.
    """
    name = "openvr"
    version = "master"
    license = "https://github.com/ValveSoftware/openvr/blob/master/LICENSE"
    url = "https://gitlab.com/HeiGameStudio/ArsenEngine/dependencies/conan-openvr"
    description = __doc__
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    branch = version

    def source(self):
        self.run("git clone https://github.com/ValveSoftware/openvr.git -b {branch} --depth 1".format(branch=self.branch))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="openvr", build_folder="openvr-build", defs={
            "BUILD_SHARED": self.options.shared,
            "USE_LIBCXX": hasattr(self.settings.compiler, "libcxx") and self.settings.compiler.libcxx
        })
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="openvr/headers/")

        # Locate where OpenVR places the libraries and binaries.
        postfix = ""

        if self.settings.os == "Windows":
            postfix += "win"
        elif self.settings.os == "Macos":
            postfix += "osx"
        else:
            postfix += "linux"

        if self.settings.arch == "x86":
            postfix += "32"
        else:
            postfix += "64"

        if self.settings.os == "Windows":
            if self.settings.build_type == "Debug":
                postfix += "/Debug"
            else:
                postfix += "/Release"

        lib_folder_name = "openvr-build/lib/" + postfix

        self.copy("*.so", dst="lib", src=lib_folder_name, keep_path=False)
        self.copy("*.lib", dst="lib", src=lib_folder_name, keep_path=False)
        self.copy("*.a", dst="lib", src=lib_folder_name, keep_path=False)

        bin_folder_name = "openvr-build/bin/" + postfix

        self.copy("*.dylib", dst="lib", src=bin_folder_name, keep_path=False)
        self.copy("*.lib", dst="lib", src=bin_folder_name, keep_path=False)
        self.copy("*.dll", dst="bin", src=bin_folder_name, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["openvr_api"]
        if self.settings.os == "Windows" and self.settings.arch != "x86":
            self.cpp_info.libs = ["openvr_api64"]

