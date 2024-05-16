import argparse
from licel_service.services import build_service
from licel_service.utils import gitlab_service
import pandas


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='CLI for interacting with project services.')
    # subparsers = parser.add_subparsers(dest='service', help='Service commands')
    #
    # # Build service
    # parser_build = subparsers.add_parser('build', help='Interact with the build service')
    # parser_build.add_argument('-p', '--param', help='Parameter for build service')
    #
    # # DPS service
    # parser_dps = subparsers.add_parser('dps', help='Interact with the dps service')
    # parser_dps.add_argument('-p', '--param', help='Parameter for dps service')
    #
    # args = parser.parse_args()
    #
    # if args.service == 'build':
    #     build_service.run(param=args.param)
    # elif args.service == 'dps':
    #     dps_service.run(param=args.param)
    # else:
    #     parser.print_help()


    gitlab_files_df = pandas.DataFrame(gitlab_service.get_all_items('glpat-x92iAryBpsxKEuZKuQs_'))

    print(gitlab_files_df.head())
    print(f'{gitlab_files_df.describe() = }')
    print(f'{gitlab_files_df.info() = }')


