"""Test cases for the __main__ module."""
from typer.testing import CliRunner

from splinterglyph import cli


def test_spling_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(cli.app)
    assert result.exit_code == 0

def test_spling_encrypt_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(cli.app, args=["encrypt", "--help"])
    assert result.exit_code == 0

def test_spling_decrypt_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(cli.app, args=["decrypt", "--help"])
    assert result.exit_code == 0
