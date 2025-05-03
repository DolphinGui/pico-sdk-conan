import os

from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain

class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "VirtualBuildEnv"

    def requirements(self):
        self.requires("picosdk/2.1.1")

    def build_requirements(self):
        self.tool_requires("pioasm/2.1.1")
        self.tool_requires("picotool/2.1.1")
    
    def generate(self):
        # copy(self, "*", self.dependencies["picosdk"].package_folder, os.path.join(self.build_folder, "sdk"))
        tc = CMakeToolchain(self)
        tc.variables["PICO_SDK_PATH"] =  self.dependencies["picosdk"].package_folder
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        defs = {
            # "PICO_SDK_PATH": os.path.join(self.build_folder, "sdk"), 
            "CMAKE_ASM_FLAGS_INIT": "-mcpu=cortex-m33 -mfloat-abi=soft",
            # "PICO_PLATFORM": "rp2350-arm-s",
            # For some reason even if I set PICO_FLASH_SIZE with PICO_BOARD=none,
            # it still doesn't work. I can't explain why.
            "PICO_BOARD": "adafruit_feather_rp2350",
        }
        cmake.configure(variables = defs)
        cmake.build()