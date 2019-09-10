from click.testing import CliRunner
from domaingistry.cli import main

# Our Main Test For Domain Name Generation CLI
def test_generate():
	runner = CliRunner()
	result = runner.invoke(main,['generate','yourdomain'])
	assert result.exit_code == 0