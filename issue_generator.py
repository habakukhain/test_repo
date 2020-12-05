
from github import Github
import os

token = os.getenv('git_token')
g = Github(token)
repo = g.get_repo("habakukhain/test_repo")

i = repo.create_issue(
    title="Issue Title",
    body="Text of the body.",
    assignee="habakukhain",
    labels=[
        repo.get_label("good first issue")
    ]
)
print(i)
