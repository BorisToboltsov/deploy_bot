import git

repo = git.Repo('/Users/boristoboltsov/project/deploy_bot', search_parent_directories=True)

repo.remote('origin').pull()

repo.git.checkout('telegram')

# repo.git.reset('--hard')