from github import Github
github = Github("ashfaquekhan", "f8d66aac85299f6ef03b8a4271a13bcec4f2c04c")
user = github.get_user()
repository = user.get_repo("UPDATE1")
file_content = repository.get_contents("Readme.md")
print(file_content.decoded_content.decode())