from conans import ConanFile, tools


class BoostProcessConan(ConanFile):
    name = "Boost.Process"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost-process"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"

    requires = \
        "Boost.Algorithm/1.65.1@bincrafters/testing", \
        "Boost.Asio/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Filesystem/1.65.1@bincrafters/testing", \
        "Boost.Fusion/1.65.1@bincrafters/testing", \
        "Boost.Iterator/1.65.1@bincrafters/testing", \
        "Boost.Move/1.65.1@bincrafters/testing", \
        "Boost.Optional/1.65.1@bincrafters/testing", \
        "Boost.System/1.65.1@bincrafters/testing", \
        "Boost.Tokenizer/1.65.1@bincrafters/testing", \
        "Boost.Type_Index/1.65.1@bincrafters/testing", \
        "Boost.Winapi/1.65.1@bincrafters/testing"

    lib_short_names = ["process"]
    is_header_only = True

    # BEGIN

    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        if self.is_header_only:
            self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
