import click
import unittest
from uvprov_api.app import init_api
from click.testing import CliRunner
from uvprov_api.uvprovapi import UVProvApplication, number_of_workers, main
from mock import patch


class TestAPIStart(unittest.TestCase):
    """Test app is ok."""

    def setUp(self):
        """Set up test fixtures."""
        self.host = '127.0.0.1'
        self.workers = number_of_workers()
        self.port = 4301
        self.log = 'logs/server.log'
        options = {
            'bind': '{0}:{1}'.format(self.host, self.port),
            'workers': self.workers,
            'daemon': 'True',
            'errorlog': self.log
        }
        self.app = UVProvApplication(init_api(), options)
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    def test_command(self):
        """Test Running from command line."""
        @click.command('server')
        @click.option('--host')
        def start(host):
            click.echo('{0}'.format(host))

        runner = CliRunner()
        result = runner.invoke(start, input=self.host)
        assert not result.exception

    @patch('uvprov_api.uvprovapi.cli')
    def test_cli(self, mock):
        """Test if cli was called."""
        main()
        self.assertTrue(mock.called)

    def running_app(self):
        """Test running app."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
