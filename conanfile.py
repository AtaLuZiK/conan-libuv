import os

from conans import CMake, ConanFile, tools


class LibuvConan(ConanFile):
    name = "libuv"
    version = "1.24.0"
    license = "MIT"
    author = "zimmerk zimmerk@live.com"
    url = "https://github.com/AtaLuZiK/conan-libuv"
    description = "libuv is a multi-platform support library with a focus on asynchronous I/O."
    topics = ("asynchronous", "events")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "libuv-config.cmake"
    generators = "cmake"

    @property
    def zip_folder_name(self):
        return "libuv-v" + self.version

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        zip_name = self.zip_folder_name + ".tar.xz"
        tools.download("https://dist.libuv.org/dist/v%(version)s/libuv-v%(version)s.tar.gz" % {'version': self.version},
                       zip_name)
        tools.check_md5(zip_name, "90320330757253b07404d2a97f59c66b")
        tools.unzip(zip_name)
        os.unlink(zip_name)

        with tools.chdir(self.zip_folder_name):
            tools.replace_in_file("CMakeLists.txt", "project(libuv)",
                                  '''project(libuv C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
            tools.replace_in_file("CMakeLists.txt", "if(UNIX)", "if(FALSE)")

    def build(self):
        with tools.chdir(self.zip_folder_name):
            tools.replace_in_file("CMakeLists.txt", "add_library(uv_a STATIC ${uv_sources})", "add_library(uv_a STATIC EXCLUDE_FROM_ALL ${uv_sources})")
            tools.replace_in_file("CMakeLists.txt", "add_library(uv SHARED ${uv_sources})", "add_library(uv ${uv_sources})")
            if not self.options.shared:
                tools.replace_in_file("CMakeLists.txt", "target_compile_definitions(uv PRIVATE ${uv_defines} BUILDING_UV_SHARED=1)", "target_compile_definitions(uv PRIVATE ${uv_defines})")
        cmake = CMake(self)
        cmake.configure(source_folder=self.zip_folder_name)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="%s/include" % self.zip_folder_name)
        self.copy("uv.lib", dst="lib", src="lib")
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.so", dst="lib", src="lib")
        self.copy("*.dylib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")
        self.copy("libuv-config.cmake", dst="cmake")

    def package_info(self):
        if not self.settings.os == "Windows":
            self.cpp_info.libs = ["libuv.a"] if self.options.shared else ["libuv.so"]
        else:
            self.cpp_info.libs = ["uv.lib"]
        self.cpp_info.defines = ["USING_UV_SHARED"] if self.options.shared else []
