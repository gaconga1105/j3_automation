import argparse
from licel_service.services import build_service, testing_service

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for interacting with project services.')
    subparsers = parser.add_subparsers(dest='service', help='Service commands')

    # Build service
    parser_build = subparsers.add_parser('build', help='Interact with the build service')
    parser_build.add_argument('-p', '--param', help='Parameter for build service')



    # # DPS service
    # parser_dps = subparsers.add_parser('dps', help='Interact with the dps service')
    # parser_dps.add_argument('-p', '--param', help='Parameter for dps service')

    # Massive Testing service
    testing_service_parser = subparsers.add_parser('test', help='Interact with the test service')
    testing_service_parser.add_argument('--dexprotector', help='Path to dexprotector.jar')
    testing_service_parser.add_argument('--configFile', help='Path to XML configuration file')
    testing_service_parser.add_argument('--binaryFile', help='Path to original binary file')
    testing_service_parser.add_argument('--protectedLoc', help='Path to protected binary location')

    args = testing_service_parser.parse_args()

    # if args.service == 'build':
    #     build_service.run(param=args.param)
    #     pass
    # elif args.service == 'test':
    #     testing_service.TestingService.batch_protect_and_build(
    #         args['configFile']
    #     )
    # else:
    #     parser.print_help()

