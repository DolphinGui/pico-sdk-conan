from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, patch, chdir
from os.path import join

class Picotool(ConanFile):
    name = "picotool"
    version = "2.1.1"
    package_type = "application"

    license = "BSD-3"
    author = "<Shin Umeda> <umeda.shin@gmail.com>"
    url = "https://github.com/DolphinGui/pico-sdk-libhal"
    description = "The Raspberry Pi Picotool repackaged for conan"
    topics = ("Embedded", "Raspberry Pi Pico", "ARM")

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "patches/*"


    def config_options(self):
        pass

    def configure(self):
        pass

    def requirements(self):
        self.requires("mbedtls/2.28.9")
        self.requires("libusb/1.0.26")

    def layout(self):
        cmake_layout(self, src_folder = 'picotool')
    
    def source(self):
        with chdir(self, ".."):
            # Downloading two sources is kinda bad, but unfortunately picotool requires the sdk for some reason
            get(self, **self.conan_data["picotool_sources"][self.version], destination = 'picotool')
            get(self, **self.conan_data["sdk_sources"][self.version], destination = 'sdk')
            patch_file = join(self.export_sources_folder, "patches/2.1.1-ptool.patch")
            patch(self, patch_file=patch_file, base_path = join(self.export_sources_folder, "picotool"))

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.preprocessor_definitions["HAS_MBEDTLS"] = "1"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        defs = {"PICO_SDK_PATH": join(self.export_sources_folder, "sdk")}
        cmake.configure(variables = defs)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        pass
