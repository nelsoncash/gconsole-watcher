import sys
import os
import git
import time
from git import Repo

def watch_git(git, repo_path, to_call):
	result = git.checkout("master")
	if result == "Your branch is up-to-date with 'origin/master'.":
		time.sleep(60)
		watch_git(git, repo_path, to_call)
	else:
		git.pull()
		time.sleep(60)
		os.system("{} {}".format(os.path.abspath(to_call), os.path.abspath(repo_path)))
		watch_git(git, repo_path, to_call)

if __name__ == '__main__':
	repo_path = str(sys.argv[1])
	to_call = str(sys.argv[2])
	repo = Repo(os.path.abspath(repo_path))
	git = repo.git

	watch_git(git, repo_path, to_call)