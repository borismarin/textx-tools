import click
import pkg_resources



class TextXCLI(click.MultiCommand):

    def list_commands(self, ctx):
        commands = []
        for ep in pkg_resources.iter_entry_points(group='textx_commands'):
            commands.append(ep.name)
        return commands

    def get_command(self, ctx, name):
        for ep in pkg_resources.iter_entry_points(group='textx_commands'):
            if ep.name == name:
                return ep.load()

textx = TextXCLI(help='textx developer tools')


