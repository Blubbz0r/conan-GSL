from conans import ConanFile

class GSLConan(ConanFile):
    name = "GSL"
    version = "0.1"

    def source(self):
       self.run("git clone https://github.com/Microsoft/GSL.git")
       self.run("cd GSL && git checkout 1c95f9436eae69c9b9315911ef6aa210df7d1e31")

    def package(self):
        self.copy("*", dst="include", src="GSL/include")