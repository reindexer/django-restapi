from setuptools import setup, find_packages
 
setup(
  name = "django-restapi",
  version = "0.1.2",
  keywords = ["pip", "api","REST", "django"],
  description = "REST api for django",
  long_description = "REST api for django",
  license = "MIT Licence",
 
  url = "https://github.com/reindexer/django-restapi",
  author = "reindexer",
  author_email = "konglingkai@metatype.cn",
 
  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = ['django'],
  package_data = {
    '': ['*.html'],
  }
)
