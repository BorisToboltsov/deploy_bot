import git

class MyGit:
    def __init__(self, path):
        self.repo = git.Repo(
            path, search_parent_directories=True
        )

    def checkout(self, path: str):
        try:
            self.repo.git.checkout(path)
        except git.exc.GitError as e:
            return e

    def pull(self):
        try:
            self.repo.remote('origin').pull()
        except git.exc.GitError as e:
            return e

    def reset(self):
        try:
            self.repo.git.reset('--hard')
        except git.exc.GitError as e:
            return e
