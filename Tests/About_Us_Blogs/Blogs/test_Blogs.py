import pytest
from Tests.test_Base import BaseTest
from Pages.About_Us_Blogs.Blogs.Blogs import Blogs
from Config.config import TestData
from CheckSSLCert import validate
import pandas as pd
import allure

@allure.title("Blog Page Test Cases")
class TestBlogs(BaseTest):

    global aboutUsObj