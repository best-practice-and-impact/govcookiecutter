from pathlib import Path
from sphinx.cmd.build import main


class TestDocumentation:
    def test_build(self, tmp_path: Path) -> None:
        """Test the build of the main `govcookiecutter` repository."""
        assert main(["-b", "html", "docs", str(tmp_path.joinpath("_build"))]) == 0

# def test_external_links(self, tmp_path: Path) -> None:
#     """Test for broken external links of the main `govcookiecutter` repository."""
#     assert (
#         main(["-b", "linkcheck", "docs", str(tmp_path.joinpath("_linkcheck"))]) == 0
#     )
