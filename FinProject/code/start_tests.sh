#!/bin/bash
pytest -s -v -l -n 3 /tmp/code/api/api_tests/test_api.py --alluredir=/tmp/code/allure-results
pytest -s -v -l /tmp/code/ui/test/test_ui.py --alluredir=/tmp/code/allure-results