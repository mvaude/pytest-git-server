# -*- coding: utf-8 -*-

"""  Repository fixtures
"""

import logging
import os

import pytest
from git import Repo


@pytest.fixture(scope="session")
def git_repo(request):
    """ Session-scoped fixture to create a new git repo in a temporary workspace.

        Attributes
        ----------
        uri (str) :  Repository URI
        api (`git.Repo`) :  Git Repo object for this repository
        .. also inherits all attributes from the `workspace` fixture

    """
    return GitRepo()


class GitRepo(object):
    """
    Creates an empty Git repository in a temporary workspace.
    Cleans up on exit.

    Attributes
    ----------
    uri : `str`
        repository base uri
    api : `git.Repo` handle to the repository
    """
    def __init__(self):
        self.workspace = os.path.expanduser('test')
        self.api = Repo.init(self.workspace)
        self.uri = "file://%s" % self.workspace
