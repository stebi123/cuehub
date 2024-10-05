import os
import click
from cuehub.utils.framework_helper import check_and_create_virtualenv, install_package, copy_template

def setup_tornado():
    """Sets up a Tornado project."""
    project_name = click.prompt('Enter your Tornado project name', type=str)

    # Check and create virtual environment
    venv_name = f"{project_name}_venv"
    check_and_create_virtualenv(venv_name)

    # Install Tornado
    install_package('tornado', venv_name)

    # Copy Tornado template
    click.echo(f'Creating Tornado project structure for "{project_name}"...')
    os.makedirs(project_name, exist_ok=True)
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'tornado_template')
    copy_template(template_path, project_name)

    click.echo(f'Tornado project "{project_name}" setup complete!')

    # Guide the user
    click.echo(f'\nNext steps:')
    click.echo(f'1. Activate your virtual environment: source {venv_name}/bin/activate')
    click.echo(f'2. Change into your project directory: cd {project_name}')
    click.echo(f'3. Run the Tornado app: python app.py')
