import os
import click
import pyfiglet
from colorama import init, Fore
from cuehub.commands import django, flask, fastapi, pyramid, tornado
from cuehub.utils.framework_helper import save_user_details, check_existing_user

@click.group()
def cue():
    """CueHub CLI - Setup frameworks like Django, Flask, etc."""
    # Create ASCII art
    ascii_art = pyfiglet.figlet_format("CueHub")

    # Center the ASCII art
    width = os.get_terminal_size().columns
    centered_ascii_art = "\n".join(line.center(width) for line in ascii_art.splitlines())

    # Print ASCII art in green
    click.echo(Fore.GREEN + centered_ascii_art)

    # Print description centered in green
    description = "CueHub is a developer tool designed to simplify project workflows and enhance productivity."
    centered_description = description.center(width)
    click.echo(Fore.GREEN + centered_description)

@cue.command()
def init():
    """Initializes CueHub in the current folder."""
    # Check if user details exist, if not prompt for user details
    if not check_existing_user():
        click.echo('Welcome to CueHub! Let\'s set things up.')

        name = click.prompt('Enter your name', type=str)
        email = click.prompt('Enter your email', type=str)
        project_name = click.prompt('Enter your project name', type=str)

        save_user_details(name, email, project_name)
        click.echo(f'Project "{project_name}" initialized successfully with your details!')
    else:
        click.echo('CueHub is already initialized with your details.')

@cue.command()
@click.argument('framework', type=click.Choice(['django', 'flask', 'fastapi', 'pyramid', 'tornado'], case_sensitive=False), required=False)
def setup(framework):
    """Setup a project with a chosen framework."""
    if framework:
        # Directly use the specified framework
        click.echo(f'Setting up {framework}...')
        if framework.lower() == 'django':
            django.setup_django()
        elif framework.lower() == 'flask':
            flask.setup_flask()
        elif framework.lower() == 'fastapi':
            fastapi.setup_fastapi()
        elif framework.lower() == 'pyramid':
            pyramid.setup_pyramid()
        elif framework.lower() == 'tornado':
            tornado.setup_tornado()
    else:
        # Prompt the user to choose a framework if not specified
        click.echo("Choose a framework to set up:")
        frameworks = ['Django', 'Flask', 'FastAPI', 'Pyramid', 'Tornado']
        choice = click.Choice(frameworks, case_sensitive=False)

        framework_choice = click.prompt('Enter the framework you want to setup', type=choice)

        # Call the respective setup function based on user input
        if framework_choice.lower() == 'django':
            django.setup_django()
        elif framework_choice.lower() == 'flask':
            flask.setup_flask()
        elif framework_choice.lower() == 'fastapi':
            fastapi.setup_fastapi()
        elif framework_choice.lower() == 'pyramid':
            pyramid.setup_pyramid()
        elif framework_choice.lower() == 'tornado':
            tornado.setup_tornado()
        else:
            click.echo('Invalid choice! Please try again.')

if __name__ == "__main__":
    cue()
