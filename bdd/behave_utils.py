from collections import OrderedDict
import re
import logging
from Buckman_UI import config

logger = logging.getLogger(config.APP_NAME)


# strip extras from hiptest/behave params to get actual bubblegum params
# needed.
def strip_behave_params(param, remove_brackets_quotes=True, change_dashes_and_spaces=True, lower_case=True,
                        change_underscores=False):
    """
    Strips the behave params to make them usable by bubblegum.  Depending on what you need the params for
    you can mix and match the removal of the curly brackets and quotes, change dashes and spaces to underscores,
    or lower the case by setting the appropriate boolean arguments.  It defaults to all True.
    """
    if remove_brackets_quotes:
        param = remove_brackets_and_quotes(param)

    if change_dashes_and_spaces:
        param = change_dashes_and_spaces_to_underscore(param)

    if change_underscores:
        param = change_underscores_to_dashes(param)

    param = param.lstrip()  # remove any leftover leading whitespace

    if lower_case:
        return param.lower()
    else:
        return param


def remove_brackets_and_quotes(param):
    """
    Removes the behave curly brackets and their contents "{<contents>}"  and any quotes.
    """
    rep = OrderedDict([("\$\{.*?\} ", ""), ("\{.*?\} ", ""), ('"', '')])
    for k, v in rep.items():
        result = re.sub(k, v, param)
        param = result
    return param


def change_dashes_and_spaces_to_underscore(param):
    """
    Changes any dashes "-" or spaces " " to underscores "_"
    """
    rep = OrderedDict([("-", "_"), (" ", "_")])
    for k, v in rep.items():
        result = re.sub(k, v, param)
        param = result
    return param


def change_underscores_to_dashes(param):
    """
    Changes any dashes "-" to underscores "_"
    """
    rep = OrderedDict([("_", "-")])
    for k, v in rep.items():
        result = re.sub(k, v, param)
        param = result
    return param


def parse_step_datatable(table):
    table_dict = {}
    for heading in table.headings:
        if table[0][heading]:
            table_dict[heading] = table[0][heading]
    return table_dict

    # Returns element on a page
