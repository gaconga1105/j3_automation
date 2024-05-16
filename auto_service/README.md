my_project/
│
├── my_project/                   # Main project package
│   ├── __init__.py               # Makes my_project a Python package
│   ├── cli.py                    # Entry point for the CLI
│   ├── config.py                 # Configuration settings and constants
│   │
│   ├── services/                 # Directory for service modules
│   │   ├── __init__.py           # Makes services a Python package
│   │   ├── base_service.py       # Base class for services
│   │   ├── build_service.py      # build_service implementation
│   │   ├── dps_service.py        # dps_service implementation
│   │   └── ...                   # Future service modules
│   │
│   └── utils/                    # Utility functions and classes
│       ├── __init__.py           # Makes utils a Python package
│       └── common_utils.py       # Common utility functions
│
├── tests/                        # Unit tests
│   ├── __init__.py
│   ├── test_build_service.py
│   ├── test_dps_service.py
│   └── ...
│
├── README.md                     # Project overview and usage
├── requirements.txt              # Project dependencies
└── setup.py                      # Installation script
