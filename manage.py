import click
import uvicorn


from service_name.app import app


@click.group()
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create database schema and tables"""
    from copy import copy
    from alembic.command import stamp
    from alembic.config import Config
    from sqlalchemy import text
    from service_name.config import get_config
    from service_name.database import engine
    from service_name.models import Base

    config = get_config()
    # functions to setup local db for development

    click.echo("Done!")


@cli.command("run")
def run():
    uvicorn.run(app, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    cli()
