import click


@click.group(short_help="embedding CLI.")
def embedding():
    """embedding CLI.
    """
    pass


@embedding.command()
@click.argument("name", default="embedding")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [embedding]
