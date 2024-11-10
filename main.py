import git

repo = git.Repo(
    "/Users/boristoboltsov/project/deploy_bot", search_parent_directories=True
)

# Git pull
# repo.remote('origin').pull()

try:
    repo.git.checkout("telegram")
except git.exc.GitError as e:
    print(e)


# Сброс всех изменений
# repo.git.reset('--hard')
