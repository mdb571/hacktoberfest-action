import os
from github import Github, UnknownObjectException
from github.Label import Label
from github.Repository import Repository
import datetime


def add_label(repo: Repository, label_filter):
    """Add hacktoberfest label to all issues labeled with filter label."""
    issues_list = repo.get_issues(state="open", labels=['label_filter'])
    for issue in issues_list:
        issue.add_to_labels("hacktoberfest")

def remove_label(repo: Repository):
    """Remove label from all issues with it."""
    issues_list = repo.get_issues(state="open", labels=['hacktoberfest'])
    for issue in issues_list:
        issue.remove_from_labels("hacktoberfest")


def new_label(
    repo: Repository,
    label_color: str,) -> Label:
    """Get the Label object or create it with given features."""
    try:
        label_to_add = repo.get_label('hacktoberfest')
    except UnknownObjectException:
        label_to_add = repo.create_label(
            name='hacktoberfest',
            color=label_color,
            description="Issues for contributing during the period of hacktoberfest",
        )
    return label_to_add





gh_repository = os.getenv("GITHUB_REPOSITORY")
gh_token = os.getenv("GITHUB_TOKEN")
label_color = os.getenv("LABEL_COLOR")
label_filter = os.getenv("LABEL_FILTER")


gh = Github(login_or_token=gh_token)
repo = gh.get_repo(gh_repository)

today = datetime.today()

if today.month==9:
    if label_filter!="":
        add_label(repo, label_filter)
    else:
        new_label(repo,label_color,)
else:
    remove_label(repo)