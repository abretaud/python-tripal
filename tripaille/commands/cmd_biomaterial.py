import click
from tripaille.commands.biomaterial.add_biomaterial import cli as func0


@click.group()
def cli():
    """Manage Tripal organisms"""
    pass


cli.add_command(func0)
