from pathlib import Path
import subprocess
import licel_service.utils.cli_handler as cli_handler

if __name__ == '__main__':

    config_folder_path = Path('/Users/licel/Downloads/test v1SigningEnabled')
    dexprotector_path = Path('/Users/licel/dexprotector-distros/dexprotector-ent-14.1.25/dexprotector.jar')
    original_binary_path = Path('/Users/licel/Test & Demo/Android/app-debug-unsigned.apk')

    for config_file in list(Path(config_folder_path).glob('*.xml')):
        protected_binary_name = f'{original_binary_path.stem}.{config_file.stem}.protected{original_binary_path.suffix}'
        protected_binary_path = config_folder_path / protected_binary_name
        log_file_path = config_folder_path / f'{protected_binary_name}.log'

        command = cli_handler.generate_dp_protection_command(dexprotector_path, config_file, original_binary_path, protected_binary_path)

        print(command)

        with open(log_file_path, mode='w') as log_file:
            result = subprocess.run(command, shell=True, stdout=log_file, stderr=log_file, text=True)
