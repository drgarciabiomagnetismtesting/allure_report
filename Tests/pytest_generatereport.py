import os
import shutil
import pytest
import allure
import boto3

# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session):
#     # Generate Allure report
#     report_dir = "Allure_Generated_Files"
#     allure_dir = os.path.join(report_dir, "allure-report")
#     shutil.rmtree(allure_dir, ignore_errors=True)
#     allure_cmd = f"allure generate {report_dir} --clean"
#     os.system(allure_cmd)

    # Upload report to S3
    # bucket_name = "<bucket_name>"
    # s3 = boto3.client("s3")
    # for root, dirs, files in os.walk(allure_dir):
    #     for file in files:
    #         local_path = os.path.join(root, file)
    #         s3_path = os.path.relpath(local_path, allure_dir)
    #         s3.upload_file(local_path, bucket_name, s3_path)

import pytest

