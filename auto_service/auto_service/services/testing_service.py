from pathlib import Path
import subprocess
from licel_service.utils.cli_handler import generate_dp_protection_command
import logging

class TestingService:


    @property
    def latest_version(self):
        pass

    def __init__(self):
        TestingServiceLoggerName = 'TestingService'
        TestingServiceLogger = logging.getLogger(TestingServiceLoggerName)
        # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
        TestingServiceLogger.setLevel(logging.INFO)

        # Create a console handler and set its logging level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the console handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Add the console handler to the logger
        TestingServiceLogger.addHandler(console_handler)

    @staticmethod
    def batch_protect_and_build(self, dexprotector_path, config_folder_path, original_binary_path, protected_binary_folder_path):

        for config_file in list(Path(config_folder_path).glob('*.xml')):
            protected_binary_name = f'{original_binary_path.stem}.{config_file.stem}.protected{original_binary_path.suffix}'
            protected_binary_path = config_folder_path / protected_binary_name
            log_file_path = config_folder_path / f'{protected_binary_name}.log'

            command = generate_dp_protection_command(dexprotector_path, config_file, original_binary_path,
                                                     protected_binary_path)

            self.TestingServiceLogger.info(f'Running command:\n {command}')

            with open(log_file_path, mode='w') as log_file:
                subprocess.run(command, shell=True, stdout=log_file, stderr=log_file, text=True)