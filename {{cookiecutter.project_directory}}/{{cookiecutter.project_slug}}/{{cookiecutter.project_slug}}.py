"""{{ cookiecutter.project_name }}."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
from time import perf_counter

from aaron_common_libs.common_funcs import argument, cli, pretty_print, subcommand
from aaron_common_libs.logger.custom_logger import CustomLogger
from config import Config

{% if cookiecutter.use_rich_console == "yes" -%}from rich.console import Console

# from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
# from rich.prompt import Prompt

console = Console(){%- endif %}
config = Config()
logging_handler = CustomLogger(log_dict=config.log_dict)
logger = logging_handler.default
logger_all = logging_handler.all


# Sub-Commands for TEST operations
@subcommand(
    [
        argument("--test1", help="This is a test!", action="store_true", required=False),
        argument("--test2", help="This is a test!", type=str, nargs=1, required=False),
    ]
)
def test(args):
    """Subcommand options for test operations."""
    logger.debug("args==%s", vars(args))
    test_results = {}
    if args.test1:
        test_results = {"foo": "bar"}
    if args.test2:
        test_results = {"foo": args.test2[0]}
    return test_results


def main():
    """Do Something."""
    start_time = perf_counter()

    logger.info("")
    logger_all.info("---------- START START START ----------")
    logger_all.info(
        "%s v%s (%s)",
        config.app_dict["title"],
        config.app_dict["version"],
        config.app_dict["date"],
    )
{% if cookiecutter.use_rich_console == "yes" %}    console.rule(f"""{config.app_dict["title"]} {config.app_dict["version"]} ({config.app_dict["date"]})"""){%- endif %}
    required_vars = {}
    find_null_vars = [value for value in required_vars.items() if None is value[1]]
    if find_null_vars:
        logger.error("Missing Environment Variable(s): %s", find_null_vars)
        print(f"\nERROR: Missing Environment Variable(s): {find_null_vars}")
    else:
        args = cli.parse_args()
        if args.subcommand is None:
            cli.print_help()
        else:
            arg_results = args.func(args)
            if arg_results:
                {% if cookiecutter.use_rich_console == "yes" -%}
                console.print(pretty_print(arg_results))
                {%- elif cookiecutter.use_rich_console == "no" -%}
                print(pretty_print(arg_results))
                {%- endif %}
            else:
                cli.print_help()
{% if cookiecutter.use_rich_console == "yes" %}    console.rule(f"""Total Execution Time: {round(perf_counter() - start_time, 2)} seconds""", style="red"){%- endif %}
    logger_all.info("Total Execution Time: %s seconds", round(perf_counter() - start_time, 2))
    logger_all.info("----------   STOP STOP STOP  ----------")
    logger.info("")


if __name__ == "__main__":
    sys.exit(main())
