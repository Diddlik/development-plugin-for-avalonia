import tempfile
import textwrap
import unittest
from pathlib import Path

from scripts.generate_api_migration_report import (
    ApiItem,
    build_added_api_section,
    normalize_target_name,
    parse_suppressions,
)


class GenerateApiMigrationReportTests(unittest.TestCase):
    def test_normalize_target_name_drops_target_prefix(self) -> None:
        self.assertEqual(
            normalize_target_name("M:Avalonia.Controls.Window.Show"),
            "Avalonia.Controls.Window.Show",
        )

    def test_parse_suppressions_dedupes_across_framework_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            api_dir = Path(temp_dir)
            path = api_dir / "Avalonia.nupkg.xml"
            path.write_text(
                textwrap.dedent(
                    """\
                    <?xml version="1.0" encoding="utf-8"?>
                    <Suppressions>
                      <Suppression>
                        <DiagnosticId>CP0002</DiagnosticId>
                        <Target>M:Avalonia.Controls.Window.Show</Target>
                        <Left>baseline/Avalonia/lib/net8.0/Avalonia.Controls.dll</Left>
                        <Right>current/Avalonia/lib/net8.0/Avalonia.Controls.dll</Right>
                      </Suppression>
                      <Suppression>
                        <DiagnosticId>CP0002</DiagnosticId>
                        <Target>M:Avalonia.Controls.Window.Show</Target>
                        <Left>baseline/Avalonia/lib/net10.0/Avalonia.Controls.dll</Left>
                        <Right>current/Avalonia/lib/net10.0/Avalonia.Controls.dll</Right>
                      </Suppression>
                    </Suppressions>
                    """
                ),
                encoding="utf-8",
            )

            entries = parse_suppressions(api_dir)

        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].package, "Avalonia")
        self.assertEqual(entries[0].diagnostic_id, "CP0002")
        self.assertEqual(entries[0].target, "M:Avalonia.Controls.Window.Show")

    def test_build_added_api_section_formats_container_separately(self) -> None:
        lines = build_added_api_section(
            "Added Public APIs",
            [
                ApiItem(
                    area="Application Model and Controls",
                    source_file="src/Avalonia.Controls/AppBuilder.cs",
                    namespace="Avalonia.Controls",
                    container="AppBuilder",
                    kind="member",
                    symbol="TextShapingSubsystemName",
                    signature="public string? TextShapingSubsystemName { get; private set; }",
                )
            ],
        )

        self.assertIn(
            "- `AppBuilder` -> `public string? TextShapingSubsystemName { get; private set; }`",
            lines,
        )


if __name__ == "__main__":
    unittest.main()
