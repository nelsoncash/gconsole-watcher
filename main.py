import sys
import os
import git
import time
import argparse
from git import Repo

def watch_git(git, repo_path, branch, run_path, interval):
	git.pull()
	result = git.checkout("{}".format(branch))
	print git.branch()
	pull = "git pull origin {}".format(branch)
	print pull
	os.system(pull)
	print "Checking {} branch for changes...".format(branch)
	# If git returns one of these, then we do not need to do a pull at this time
	if result != "Your branch is up-to-date with 'origin/{}'.".format(branch) and result != "Already up-to-date.":
		print "Updating local '{}' repo".format(branch)
		#git.pull()
		os.system("{} {}".format(os.path.abspath(run_path), os.path.abspath(repo_path)))
	# Wait before checking the repo so that we aren't spamming the server
	time.sleep(interval)
	watch_git(git, repo_path, branch, run_path, interval)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Watch a git repo for changes and pulls the changes")
	# The path to the repo tha we want to watch
	parser.add_argument('--repo_path', metavar='repo_path', type=str)
	# The path to the script or file to run after a git pull
	parser.add_argument('--run_path', metavar='run_path', type=str)
	# The interval time (in seconds) in between status checks on the repo
	parser.add_argument('--interval', metavar='interval', type=int)
	# The branch that we wish to watch
	parser.add_argument('--branch', metavar='branch', type=str)

	args = parser.parse_args()
	repo_path = args.repo_path
	run_path = args.run_path
	interval = args.interval
	branch = args.branch
	repo = Repo(os.path.abspath(repo_path))
	git = repo.git

	watch_git(git, repo_path, branch, run_path, interval)