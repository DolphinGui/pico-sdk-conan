from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import collect_libs
from conan.tools.files import get, replace_in_file, patch, load, copy
import os

class PicoSDK(ConanFile):
    name = "raspberry_pi_pico_sdk"
    version = "2.1.1"
    package_type = "static-library"

    # Optional metadata
    license = "BSD-3"
    author = "<Put your name here> <And your email here>"
    url = "https://github.com/DolphinGui/pico-sdk-libhal"
    description = "The Raspberry Pi Pico C/C++ SDK repackaged for conan"
    topics = ("Embedded", "Raspberry Pi Pico", "ARM")

    settings = "os", "compiler", "build_type", "arch"
    options = {"platform": ["rp2350-arm-s", "rp2040"]}
    default_options = {"platform": "rp2350-arm-s"}

    exports_sources = "patches/*"

    def config_options(self):
        pass

    def configure(self):
        pass

    def layout(self):
        cmake_layout(self)
    
    def source(self):
        get(self, **self.conan_data["sources"][self.version])
        patch_file = os.path.join(self.export_sources_folder, "patches/2.1.1-psdk.patch")
        patch(self, patch_file=patch_file)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        defs = {"PICO_BOARD": "none", 
            "PICO_PLATFORM": self.options.get_safe("platform"),
            "PICO_SDK_TESTS_ENABLED": "0",
            "CMAKE_TRY_COMPILE_TARGET_TYPE": "STATIC_LIBRARY"
        }
        cmake.configure(variables = defs)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        include_list = load(self, 'INCLUDELIST.txt')
        package_include =  os.path.join(self.package_folder, "include")
        for include in include_list.split(';'):
            copy(self, "*", include, package_include)

    def package_info(self):
        pass
