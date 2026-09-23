import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from aoc.cli import app


class CreateCommandTests(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_root_shows_create_command(self):
        result = self.runner.invoke(app, [])

        self.assertEqual(result.exit_code, 2)
        self.assertIn("create", result.output)

    @patch("aoc.cli.create_aoc_template")
    def test_create_with_explicit_options(self, create_template):
        result = self.runner.invoke(app, ["create", "-y", "2024", "-d", "5"])

        self.assertEqual(result.exit_code, 0, result.output)
        create_template.assert_called_once_with(str(Path.cwd()), "2024", "5")

    @patch("aoc.cli.create_aoc_template")
    def test_only_missing_day_is_prompted(self, create_template):
        result = self.runner.invoke(app, ["create", "-y", "2024"], input="5\n")

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertNotIn("Year", result.output)
        create_template.assert_called_once_with(str(Path.cwd()), "2024", "5")

    @patch("aoc.cli.create_aoc_template")
    def test_only_missing_year_is_prompted(self, create_template):
        result = self.runner.invoke(app, ["create", "-d", "5"], input="2024\n")

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertNotIn("Day", result.output)
        create_template.assert_called_once_with(str(Path.cwd()), "2024", "5")

    @patch("aoc.cli.datetime")
    @patch("aoc.cli.create_aoc_template")
    def test_defaults_to_previous_event_outside_december(self, create_template, mock_datetime):
        mock_datetime.now.return_value = datetime(2026, 9, 30)

        result = self.runner.invoke(app, ["create"], input="\n\n")

        self.assertEqual(result.exit_code, 0, result.output)
        create_template.assert_called_once_with(str(Path.cwd()), "2025", "1")

    @patch("aoc.cli.create_aoc_template")
    def test_invalid_options_do_not_create_files(self, create_template):
        for options in (["-y", "2014", "-d", "5"],
                        ["-y", "2024", "-d", "0"],
                        ["-y", "2024", "-d", "26"],
                        ["-y", "invalid", "-d", "5"]):
            with self.subTest(options=options):
                result = self.runner.invoke(app, ["create", *options])
                self.assertNotEqual(result.exit_code, 0)
                self.assertIn("Error:", result.output)

        create_template.assert_not_called()


if __name__ == "__main__":
    unittest.main()