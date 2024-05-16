
from licel_service.config import DexProtectorConfig


def generate_dp_protection_command(dexprotector_path, config_file_path, original_binary_path,
                                   protected_binary_path) -> str:
    class_path = (
        DexProtectorConfig.DP_ANDROID_CLASS_PATH
        if original_binary_path.suffix in DexProtectorConfig.ANDROID_FILE_EXTENSIONS
        else DexProtectorConfig.DP_IOS_CLASS_PATH
    )

    return (
        f'java -cp "{dexprotector_path}" {class_path} '
        f'-verbose '
        f'-configFile "{config_file_path}" '
        f'"{original_binary_path}" '
        f'"{protected_binary_path}"'
    )
