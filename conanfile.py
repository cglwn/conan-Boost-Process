from conans import ConanFile, tools
import os

class BoostProcessConan(ConanFile):
    name = "Boost.Process"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-process"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["process"]
    requires =  "Boost.Algorithm/1.65.1@bincrafters/stable", \
                      "Boost.Asio/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Filesystem/1.65.1@bincrafters/stable", \
                      "Boost.Fusion/1.65.1@bincrafters/stable", \
                      "Boost.Iterator/1.65.1@bincrafters/stable", \
                      "Boost.Move/1.65.1@bincrafters/stable", \
                      "Boost.Optional/1.65.1@bincrafters/stable", \
                      "Boost.System/1.65.1@bincrafters/stable", \
                      "Boost.Tokenizer/1.65.1@bincrafters/stable", \
                      "Boost.Type_Index/1.65.1@bincrafters/stable", \
                      "Boost.Winapi/1.65.1@bincrafters/stable"

                      #algorithm9 asio14 config0 core2 filesystem8 fusion5 iterator5 move3 optional5 system3 tokenizer6 type_index5 winapi1
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()