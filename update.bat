@echo off
echo Checking prerequisites.

REM try to determine if the user downloaded as .zip from github
if exist .git (
  echo Updating...
  git pull
) else (
  REM if they didn't pull a git repo, probably they don't have git
  echo This is a stationary download, can't pull updates from Github. Please download the repo again to update it.
)
