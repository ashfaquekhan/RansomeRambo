from github import Github

# Authenticate yourself 
g = Github("ashfaquekhan", "f8d66aac85299f6ef03b8a4271a13bcec4f2c04c")

# Find your repository and path of README.md
repo=g.get_user().get_repo("UPDATE1")
file = repo.get_contents("Readme.md")
# The new contents of your README.md
content = "ENCRYPT"

# Update README.md
repo.update_file("Readme.md", "commit message", content, file.sha)