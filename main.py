import sys
import os
import git
import time
from git import Repo

def check_git_status(git, branch, starting_branch):
	result = git.checkout(branch)
	if result == "Your branch is up-to-date with 'origin/master'.":
		time.sleep(60)
		check_git_status(git, branch, starting_branch)
	else:
		git.pull()
		revert_git_state(git, starting_branch)

def revert_git_state(git, branch):
	git.checkout(branch)
	git.pull()
	print "Reverted back to '{}'".format(branch)

if __name__ == '__main__':
	repo_path = str(sys.argv[1])
	repo_branch = str(sys.argv[2])
	repo = Repo(os.path.abspath(repo_path))
	git = repo.git
	starting_branch = repo.active_branch

	import atexit
	atexit.register(revert_git_state, git, starting_branch.name)

	check_git_status(git, repo_branch, starting_branch.name)
	