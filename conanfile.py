# The MIT License (MIT)
#
# Copyright (c) 2017 Mateusz Pusz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from conans import ConanFile, CMake, tools
import os

class GoogleBenchmarkConan(ConanFile):
    name = "google-benchmark"
    version = "1.3.0"
    license = "https://github.com/google/benchmark/blob/master/LICENSE"
    url = "https://github.com/mpusz/conan_google_benchmark"
    description = "A microbenchmark support library"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"

    def source(self):
        zip_name = "v%s.zip" % self.version
        url = "https://github.com/google/benchmark/archive/%s" % zip_name
        tools.download(url, zip_name)
        tools.unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["benchmark"]
