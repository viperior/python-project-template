"""Test the project's code quality using pylint"""

import logging
import os

from pylint import epylint as lint


def test_python_code_quality() -> None:
    """Run the project's source code through pylint and assert 0 errors should exist"""
    current_working_directory = os.path.basename(os.getcwd())
    command_options = f"../{current_working_directory} --disable=C0103"
    (pylint_stdout, pylint_stderr) = lint.py_run(command_options=command_options, return_std=True)
    standard_output_data = pylint_stdout.read()
    standard_error_data = pylint_stderr.read()
    logging.debug("pylint_stderr = \n%s", standard_error_data)
    pylint_error_free_search_phrase = "Your code has been rated at 10.00/10"
    pylint_errors_detected = pylint_error_free_search_phrase not in standard_output_data

    if pylint_errors_detected:
        logging.error("Pylint errors detected:\n%s", standard_output_data)

    assert pylint_error_free_search_phrase in standard_output_data
