import os

import fixtup

from alfred import manifest


def test_lookup_venv_should_return_none_when_no_venv():
    with fixtup.up('project'):
        assert manifest.lookup_venv() is None


def test_lookup_venv_should_return_venv_when_it_is_defined():
    with fixtup.up('multiproject'):
        root_path = os.getcwd()

        expected_venv_path = os.path.realpath(os.path.join(root_path, 'products', 'product1', '.venv'))
        assert manifest.lookup_venv(os.path.join(root_path, 'products', 'product1')) == expected_venv_path


def test_lookup_venv_should_return_none_when_venv_is_undefined():
    with fixtup.up('multiproject'):
        root_path = os.getcwd()

        assert manifest.lookup_venv(os.path.join(root_path, 'products', 'product2')) is None


def test_name_should_return_parent_directory_name_when_name_parameter_is_missing_in_manifest():
    """
    The name of a project is the name of the parent directory if the name parameter is missing from the manifest.

    """
    # Arrange
    with fixtup.up('project'):
        # Acts
        project_name = manifest.name()

        # Assert
        directory_name = os.path.basename(os.getcwd())
        assert project_name == directory_name


def test_prefix_should_return_specified_prefix():
    with fixtup.up('project'):
        assert manifest.prefix() == "cmd:"


def test_project_commands_pattern_should_return_default_value():
    with fixtup.up('project'):
        assert manifest.project_commands() == ["alfred/*.py"]


def test_project_commands_pattern_should_return_specified_values():
    with fixtup.up('project_with_command'):
        assert manifest.project_commands() == ["customdir/*.py"]

def test_python_path_extends_should_return_a_list_of_directory():
    with fixtup.up('pythonpath_extends'):
        assert manifest.pythonpath_extends() == ["tests"]
