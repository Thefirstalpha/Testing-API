import os


def get_managed_region() -> str:
    return os.environ['REGION']