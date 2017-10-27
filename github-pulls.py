import argparse
import getpass

from termcolor import colored
import github


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True, help="Github username")
    return parser.parse_args()


def main():
    args = parse_args()
    password = getpass.getpass("Enter Github password: ")
    g = github.Github(args.username, password)
    user = g.get_user()
    for repo in user.get_repos():
        pulls = repo.get_pulls()
        pulls = [pull for pull in pulls]
        if pulls:
            print colored(repo.full_name, 'green')
            for pull in pulls:
                print '  ' + colored(pull.title, 'red') + ' ' + colored('[' + pull.user.login + ']', 'yellow')


if __name__ == "__main__":
    main()
