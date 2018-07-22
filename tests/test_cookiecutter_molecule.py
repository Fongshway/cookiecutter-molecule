import pytest


@pytest.fixture
def baked_project(cookies):
    result = cookies.bake(extra_context={'role_name': 'helloworld'})
    return result


def test_bake_project(baked_project):
    assert baked_project.exit_code == 0
    assert baked_project.exception is None
    assert baked_project.project.basename == 'helloworld'
    assert baked_project.project.isdir()


def test_readme(baked_project):
    readme_file = baked_project.project.join('README.md')
    readme_lines = readme_file.readlines(cr=False)

    assert readme_lines[0] == 'helloworld'
