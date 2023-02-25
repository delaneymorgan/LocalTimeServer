#!/usr/bin/env python
# coding=utf-8

import argparse
import PackageBuilder

# =============================================================================


BUILD_INFO_FILENAME = "LocalTimeServer_file_list.json"


def arg_parser():
    """
    parse arguments

    :return: the parsed command line arguments
    """
    parser = argparse.ArgumentParser(description="makes LocalTimeServer a package for the specified target",
                                     add_help=False)
    parser.add_argument("-v", "--version", type=int, help="version#, i.e. x.y.z", required=True)
    parser.add_argument("-?", "--help", help="show help message and quit", action="help")
    args = parser.parse_args()
    return args


def main():
    args = arg_parser()
    try:
        builder = PackageBuilder.PackageBuilder("LocalTimeServer", BUILD_INFO_FILENAME, args.version)
        builder.build_debian()
    except Exception as ex:
        print(f"Error: {ex}")
    return


if __name__ == '__main__':
    main()