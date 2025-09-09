from conan import ConanFile
from conan.tools.files import get, patch, copy, chdir
from os.path import join

class PicoSDK(ConanFile):
    name = "picosdk"
    version = "2.2.0"
    package_type = "static-library"

    # Optional metadata
    license = "BSD-3"
    author = "<Shin Umeda> <umeda.shin@gmail.com>"
    url = "https://github.com/DolphinGui/pico-sdk-libhal"
    description = "The Raspberry Pi Pico C/C++ SDK repackaged for conan"
    topics = ("Embedded", "Raspberry Pi Pico", "ARM")

    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = {}

    exports_sources = "patches/*"
    
    def source(self):
        get(self, **self.conan_data["sources"][self.version]["sdk"], strip_root = True)
        patch_file = join(self.export_sources_folder, f"patches/{self.version}-psdk.patch")
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

