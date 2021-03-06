# -*- coding: utf-8 -*-
from pytest_git_server import git_repo, GitRepo

def test_basic_usage(git_repo):
    hello = git_repo.workspace + '/hello.txt'
    #hello.write_text('hello world!')
    #git_repo.run('git add hello.txt')
    #git_repo.api.index.commit("Initial commit")
    #assert "Initial commit" in git_repo.api.git.log()
    # The fixture has a URI property you can use in downstream systems
    assert isinstance(git_repo, GitRepo)
    assert git_repo.uri.startswith('file://')
