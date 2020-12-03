import click
import pandas as pd
from eganalyze import __version__
from eganalyze.lib import EgData


@click.group()
@click.version_option(
    __version__, '--version', message="%(prog)s, version %(version)s"
)
def main():
    pass


@main.command()
@click.argument('input', type=click.Path(exists=True))
def analyze(input):

    data = EgData(pd.read_csv(input))

    click.echo(
        'Mean interest rate: {0:.4f}%'.format(data.mean_interest_rate)
    )
    click.echo(
        'Weighted mean interest rate: {0:.4f}%'.format(data.weighted_mean_interest_rate)
    )