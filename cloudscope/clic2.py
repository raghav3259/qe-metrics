import click
from git import GithubManager


@click.command()
@click.option('--job_url', help="enter your user name")
@click.option('--user',
              help="enter the api key which will be something,like this:" +
              "cfe5f5f96fcba8979f2f9c30e33d5372")
@click.option('--password',
              help="enter the jenkin url where all the jobs are kept")
def call_github_manager(job_url, user, password):
    gh = GithubManager(job_url, user, password)
    gh.get_response(gh.get_pull())


if __name__ == '__main__':
    call_github_manager()
