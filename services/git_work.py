import git


class GitObject:
    def __init__(self, path):
        try:
            self.repo = git.Repo(path, search_parent_directories=True)
        except git.NoSuchPathError as e:
            self.repo = None

    async def checkout(self, branch_name: str):
        try:
            self.repo.git.checkout(branch_name)
        except git.exc.GitError as e:
            return e

    async def pull(self):
        try:
            self.repo.remote("origin").pull()
        except git.exc.GitError as e:
            return e

    async def status(self):
        try:
            return self.repo.git.status()
        except git.exc.GitError as e:
            return e

    async def reset(self):
        try:
            self.repo.git.reset("--hard")
        except git.exc.GitError as e:
            return e
