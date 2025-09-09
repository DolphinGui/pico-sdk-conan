from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, patch, chdir, rmdir
import os
import shutil

class PioASM(ConanFile):
    name = "pioasm"
    package_type = "application"

    # Optional metadata
    license = "BSD-3"
    author = "<Shin Umeda> <umeda.shin@gmail.com>"
    url = "https://github.com/DolphinGui/pico-sdk-libhal"
    description = "The Raspberry Pi Pico Pio Assembler repackaged for conan"
    topics = ("Embedded", "Raspberry Pi Pico", "ARM")

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "patches/*"

    # apparently kind of optional? May or may not be interested in
    # regenerating the lexer, but let's not for now
    # def requirements(self):
    #     self.requires("bison/3.8.2")
    #     self.requires("flex/2.6.4")

    def config_options(self):
        pass

    def configure(self):
        pass

    def layout(self):
        cmake_layout(self)
    
    def source(self):
        get(self, **self.conan_data["sources"][self.version], destination = 'sdkroot', strip_root = not self.version.startswith('2.1'))
        patch_file = os.path.join(self.export_sources_folder, f"patches/{self.version}-pioasm.patch")
        patch(self, patch_file=patch_file, base_path = './sdkroot')
        with chdir(self, "./sdkroot/tools/pioasm"):
            destination = self.source_folder
            files_list = os.listdir('.')
            for files in files_list:
                shutil.move(files, destination)
        rmdir(self, 'sdkroot')

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.cache_variables['PIOASM_VERSION_STRING'] = str(self.version)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        pass
