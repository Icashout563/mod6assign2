import typer

app = typer.Typer()

# @app.command()
# def run():
#     print("Airbnb CLI running")
#
# if __name__ == "__main__":
#     app()

from typer.testing import CliRunner

from cli import app

import pytest

runner = CliRunner()


def test_filter_price_command():
    result = runner.invoke(app, ["filter-price", "--min-price", "50", "--max-price", "200"])

    assert result.exit_code == 0

    assert "Cozy Apartment" in result.output


def test_export_json_command(tmp_path):
    filename = str(tmp_path / "output.json")

    result = runner.invoke(app, ["export-json", filename])

    assert result.exit_code == 0

    assert "Exported to" in result.output
