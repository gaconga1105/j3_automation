class DexProtectorConfig:
    ANDROID_FILE_EXTENSIONS = ['.apk', '.aar']
    IOS_FILE_EXTENSIONS =['.ipa', '.framework', '.xcframework', '.xcarchive']
    DP_ANDROID_CLASS_PATH = 'com.licel.dexprotector.ConsoleTask'
    DP_IOS_CLASS_PATH = 'com.licel.dexprotector.ios.ConsoleTask'