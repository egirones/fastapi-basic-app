"""
Name: Unknownw
Date: 21.03.2023
Sanity check
"""

from os import path

import argparse
import importlib
import inspect
import os
import sys

fail_color = '\033[91m'
ok_color = '\033[92m'
warn_color = '\033[93m'


def run_sanity_check(test_dir):

    # assert path.isdir(test_dir), 
    # fail_color+f"No direcotry named {test_dir} found in {os.getcwd()}"
    print('This script will perform a sanity test \
          to ensure your code meets the criteria in the rubric.\n')
    print('Please enter the path to the file that')
    print('contains your test cases for the \
          GET() and POST() methods')
    print('The path should be something\
          like abc/def/test_xyz.py')
    filepath = input('> ')

    assert path.exists(filepath), f"File {filepath} does not exist."
    sys.path.append(path.dirname(filepath))

    module_name = path.splitext(path.basename(filepath))[0]
    module = importlib.import_module(module_name)

    test_function_names = list(
        filter(
            lambda x: inspect.isfunction(
                getattr(
                    module,
                    x)) and not x.startswith('__'),
            dir(module)))

    test_functions_for_get = list(
        filter(
            lambda x: inspect.getsource(
                getattr(
                    module,
                    x)).find('.get(') != -1,
            test_function_names))
    test_functions_for_post = list(
        filter(
            lambda x: inspect.getsource(
                getattr(
                    module,
                    x)).find('.post(') != -1,
            test_function_names))

    print("\n============= Sanity Check Report ===========")
    sanity_test_passing = True
    warning_count = 1

    # GET()
    test_for_get_method_response_code = False
    test_for_get_method_response_body = False
    if not test_functions_for_get:
        print(fail_color + f"[{warning_count}]")
        warning_count += 1
        print(fail_color + "No test cases were detected \
              for the GET() method.")
        print(
            fail_color +
            "\nPlease make sure you have a test case for the GET method.\
            This MUST test both the status code as well as the contents \
            of the request object.\n")
        sanity_test_passing = False

    else:
        for func in test_functions_for_get:
            source = inspect.getsource(getattr(module, func))
            if source.find('.status_code') != -1:
                test_for_get_method_response_code = True
            if (source.find('.json') != -1) or (source.find('json.loads') != -1):
                test_for_get_method_response_body = True

        if not test_for_get_method_response_code:
            print(fail_color + f"[{warning_count}]")
            warning_count += 1
            print(
                fail_color +
                "Your test case for GET() does not seem to \
                be testing the response code.\n")

        if not test_for_get_method_response_body:
            print(fail_color + f"[{warning_count}]")
            warning_count += 1
            print(
                fail_color +
                "Your test case for GET() does not seem to \
                    be testing the CONTENTS of the response.\n")

    # POST()
    test_for_post_method_response_code = False
    test_for_post_method_response_body = False
    count_post_method_for_inference_result = 0

    if not test_functions_for_post:
        print(fail_color + f"[{warning_count}]")
        warning_count += 1
        print(fail_color + "No test cases were detected\
            for the POST() method.")
        print(
            fail_color +
            "Please make sure you have TWO test cases\
                for the POST() method." +
            "\nOne test case for EACH of the possible\
                inferences (results/outputs) of the ML model.\n")
        sanity_test_passing = False
    else:
        if len(test_functions_for_post) == 1:
            print(f"[{warning_count}]")
            warning_count += 1
            print(
                fail_color +
                "Only one test case was detected\
                    for the POST() method.")
            print(
                fail_color +
                "Please make sure you have two test\
                    cases for the POST() method." +
                "\nOne test case for EACH of the possible]\
                    inferences (results/outputs) of the ML model.\n")
            sanity_test_passing = False

        for func in test_functions_for_post:
            source = inspect.getsource(getattr(module, func))
            if source.find('.status_code') != -1:
                test_for_post_method_response_code = True
            if (source.find('.json') != -1) or (source.find('json.loads') != -1):
                test_for_post_method_response_body = True
                count_post_method_for_inference_result += 1

        if not test_for_post_method_response_code:
            print(fail_color + f"[{warning_count}]")
            warning_count += 1
            print(
                fail_color +
                "One or more of your test cases for POST()\
                    do not seem to be testing the response code.\n")
        if not test_for_post_method_response_body:
            print(fail_color + f"[{warning_count}]")
            warning_count += 1
            print(
                fail_color +
                "One or more of your test cases for POST() do\
                    not seem to be testing the contents of the response.\n")

        if len(
                test_functions_for_post
            ) >= 2 and count_post_method_for_inference_result < 2:
            print(fail_color + f"[{warning_count}]")
            warning_count += 1
            print(
                fail_color +
                "You do not seem to have TWO separate test cases,\
                    one for each possible prediction that your model can make.")

    sanity_test_passing = sanity_test_passing and\
        test_for_get_method_response_code and \
        test_for_get_method_response_body and \
        test_for_post_method_response_code and \
        test_for_post_method_response_body and \
        count_post_method_for_inference_result >= 2

    if sanity_test_passing:
        print(ok_color + "Your test cases look good!")

    print(
        warn_color +
        "This is a heuristic based sanity testing and cannot\
            guarantee the correctness of your code.")
    print(
        warn_color +
        "You should still check your work against the rubric\
            to ensure you meet the criteria.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'test_dir',
        metavar='test_dir',
        nargs='?',
        default='tests',
        help='Name of the directory that has test files.')
    args = parser.parse_args()
    run_sanity_check(args.test_dir)
