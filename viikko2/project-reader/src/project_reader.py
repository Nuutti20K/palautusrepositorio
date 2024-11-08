from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed = toml.loads(content)

        name = parsed["tool"]["poetry"]["name"]
        description = parsed["tool"]["poetry"]["description"]
        dependencies = list(parsed["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(parsed["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())
        license = parsed["tool"]["poetry"]["license"]
        authors = list(parsed["tool"]["poetry"]["authors"])


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
