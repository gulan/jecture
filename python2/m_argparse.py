#!/usr/bin/env python

import argparse
import sys

# need to capture io

if 0:
    for i in dir(argparse):
        if i.startswith('_'):
            continue
        print i, type(argparse.__dict__[i])

def argparse_00():
    # Examine module content
    assert argparse.ONE_OR_MORE == '+'
    assert argparse.OPTIONAL == '?'
    assert argparse.PARSER == 'A...'
    assert argparse.REMAINDER == '...'
    assert argparse.SUPPRESS == '==SUPPRESS=='
    assert argparse.ZERO_OR_MORE == '*'
    assert isinstance(argparse.Action, type)
    assert isinstance(argparse.ArgumentDefaultsHelpFormatter, type)
    assert isinstance(argparse.ArgumentError, type)
    assert isinstance(argparse.ArgumentParser, type)
    assert isinstance(argparse.ArgumentTypeError, type)
    assert isinstance(argparse.FileType, type)
    assert isinstance(argparse.HelpFormatter, type)
    assert isinstance(argparse.Namespace, type)
    assert isinstance(argparse.RawDescriptionHelpFormatter, type)
    assert isinstance(argparse.RawTextHelpFormatter, type)
    print 'argparse_00 ok'

def argparse_01():
    assert argparse.Namespace(x=1).x == 1
    assert (vars(argparse.Namespace(x=1, y='abc', z=(2,3,4))) 
            == {'y': 'abc', 'x': 1, 'z': (2, 3, 4)})
    assert argparse.Namespace(x=13)._get_kwargs() == [('x', 13)]
    print 'argparse_01 ok'

# 'add_argument', 'add_argument_group', 'add_help', 'add_mutually_exclusive_group', 'add_subparsers', 'argument_default', 'conflict_handler', 'convert_arg_line_to_args', 'description', 'epilog', 'error', 'exit', 'format_help', 'format_usage', 'format_version', 'formatter_class', 'fromfile_prefix_chars', 'get_default', 'parse_args', 'parse_known_args', 'prefix_chars', 'print_help', 'print_usage', 'print_version', 'prog', 'register', 'set_defaults', 'usage', 'version'

# _action_groups <type 'list'>
# _actions <type 'list'>
# _defaults <type 'dict'>
# _has_negative_number_optionals <type 'list'>
# _mutually_exclusive_groups <type 'list'>
# _negative_number_matcher <type '_sre.SRE_Pattern'>
# _option_string_actions <type 'dict'>
# _optionals <class 'argparse._ArgumentGroup'>
# _positionals <class 'argparse._ArgumentGroup'>
# _registries <type 'dict'>
# _subparsers <type 'NoneType'>

    
def argparse_02():
    # All args with defaults
    p = argparse.ArgumentParser(
        prog=None, 
        usage=None, 
        description=None, 
        epilog=None, 
        parents=[], 
        formatter_class=argparse.HelpFormatter, 
        prefix_chars='-', 
        fromfile_prefix_chars=None, 
        argument_default=None, 
        conflict_handler='error', 
        version = None,
        add_help=True)
    assert p.add_help == True
    assert p.argument_default == None
    assert p.conflict_handler == 'error'
    assert p.description == None
    assert p.epilog == None
    assert p.fromfile_prefix_chars == None
    assert p.prefix_chars == '-'
    assert p.prog  == 'm_argparse.py'
    assert p.usage == None
    assert p.version == None
    assert isinstance(p.formatter_class, type)

    p = argparse.ArgumentParser()
    assert p.add_help == True
    assert p.argument_default == None
    assert p.conflict_handler == 'error'
    assert p.description == None
    assert p.epilog == None
    assert p.fromfile_prefix_chars == None
    assert p.prefix_chars == '-'
    assert p.prog  == 'm_argparse.py'
    assert p.usage == None
    assert p.version == None
    assert isinstance(p.formatter_class, type)
    print 'argparse_02 ok'

def argparse_03():
    p = argparse.ArgumentParser(
        prog='prog', 
        usage='usage', 
        description='description', 
        epilog='epilog', 
        parents=[], 
        formatter_class=argparse.HelpFormatter, 
        prefix_chars='-+', 
        fromfile_prefix_chars=None, 
        argument_default=0, 
        conflict_handler='error',
        version = '1.2.3',              # Undocumented. Depreciated?
        add_help=True)
    assert p.add_help == True
    assert p.argument_default == 0
    assert p.conflict_handler == 'error'
    assert p.description == 'description'
    assert p.epilog == 'epilog'
    assert p.fromfile_prefix_chars == None
    assert p.prefix_chars == '-+'
    assert p.prog  == 'prog'
    assert p.usage == 'usage'
    assert p.version == '1.2.3'
    print 'argparse_03 ok'

# pa = p.parse_args()

if __name__ == '__main__':
    argparse_00()
    argparse_01()
    argparse_02()
    argparse_03()


