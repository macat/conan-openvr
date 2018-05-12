from conans import ConanFile, CMake, tools
from utils import SourceDownloader, GitRepository, GithubRepository


class OpenvrConan(ConanFile):
    name = "openvr"
    version = "1.0.14"
    description = "API and runtime that allows access to VR hardware from multiple vendors without requiring that " + \
                  "applications have specific knowledge of the hardware they are targeting."
    url = "https://gitlab.com/ArsenStudio/ArsenEngine/dependencies/conan-{0}".format(name)
    homepage = "https://github.com/ValveSoftware/openvr"

    license = "BSD 3-Clause"

    exports = ["LICENSE.md"]

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False]
    }
    default_options = "shared=False"

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    branch = ("v" if version != "master" else "") + version

    def source(self):
        downloader = SourceDownloader(self)

        downloader.addRepository(GitRepository(self, "https://github.com/ValveSoftware/openvr.git", branch=self.branch))
        downloader.addRepository(GithubRepository(self, "ValveSoftware/openvr", self.branch))

        downloader.get(self.source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder, defs={
            "BUILD_SHARED": self.options.shared,
            "USE_LIBCXX": hasattr(self.settings.compiler, "libcxx") and self.settings.compiler.libcxx
        })
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        self.copy("*.h", dst="include", src=self.source_subfolder + "/headers/")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
