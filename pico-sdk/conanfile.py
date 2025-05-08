from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import collect_libs
from conan.tools.files import get, replace_in_file, patch, load, copy, chdir
from os.path import join

class PicoSDK(ConanFile):
    name = "picosdk"
    version = "2.1.1"
    package_type = "static-library"

    # Optional metadata
    license = "BSD-3"
    author = "<Put your name here> <And your email here>"
    url = "https://github.com/DolphinGui/pico-sdk-libhal"
    description = "The Raspberry Pi Pico C/C++ SDK repackaged for conan"
    topics = ("Embedded", "Raspberry Pi Pico", "ARM")

    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = {}

    exports_sources = "patches/*"
    
    def source(self):
        get(self, **self.conan_data["sources"][self.version]["sdk"])
        patch_file = join(self.export_sources_folder, "patches/2.1.1-psdk.patch")
        patch(self, patch_file=patch_file)
        with chdir(self, "lib"):
            get(self, **self.conan_data["sources"][self.version]["tinyusb"], destination = "tinyusb", strip_root = True)

    def package(self):
        copy(self, "*", self.export_sources_folder, self.package_folder)
        
    def package_info(self):
        self.buildenv_info.define("PICO_SDK_PATH", self.package_folder)
        self.cpp_info.includedirs = []  # no actual include directories
        self.cpp_info.libdirs = [] # nothing is being built

    def package_id(self):
        self.info.settings.clear()

