import os
from github import Github, UnknownObjectException
from github.Label import Label
from github.Repository import Repository
from datetime import datetime

def add_label(repo: Repository, label_filter,label_to_add: Label):
    """Add hacktoberfest label to all issues labeled with filter label."""
    if label_filter!="None":
        issues_list = repo.get_issues(state="open",labels=[label_filter])
    elif label_filter=="None":
        issues_list = repo.get_issues(state="open")
    for issue in issues_list:
        issue.add_to_labels(label_to_add)

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

if today.month==10:
    label_to_add=new_label(repo,label_color)
    add_label(repo, label_filter,label_to_add)
    print('Hacktoberfest label added')
else:
    remove_label(repo)
