from click.testing import CliRunner

runner = CliRunner()


def test_hyperfocus_handle_errors(hyperfocus_cli):
    result = runner.invoke(hyperfocus_cli, [])

    expected = "✘(error) Dummy group error\n"
    assert expected == result.output


def test_hyperfocus_command_handle_errors(hyperfocus_cli):
    result = runner.invoke(hyperfocus_cli, ["bar"])

    expected = "✘(foo) Dummy command error\n"
    assert expected == result.output


def test_hyperfocus_command_handle_errors_with_click_error(hyperfocus_cli):
    result = runner.invoke(hyperfocus_cli, ["hello"])

    expected = "✘(usage error) No such command 'hello'\n"
    assert expected == result.output
