from conans import ConanFile, tools, os

class BoostProcessConan(ConanFile):
    name = "Boost.Process"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/process"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "process"
    requires =  "Boost.Algorithm/1.64.0@bincrafters/testing", \
                      "Boost.Asio/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Filesystem/1.64.0@bincrafters/testing", \
                      "Boost.Fusion/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.System/1.64.0@bincrafters/testing", \
                      "Boost.Tokenizer/1.64.0@bincrafters/testing", \
                      "Boost.Type_Index/1.64.0@bincrafters/testing", \
                      "Boost.Winapi/1.64.0@bincrafters/testing"

                      #algorithm9 asio14 config0 core2 filesystem8 fusion5 iterator5 move3 optional5 system3 tokenizer6 type_index5 winapi1
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()