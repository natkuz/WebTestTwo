import yaml
import pytest
from module import Site

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def selector_input_login():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def selector_input_password():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def selector_button():
    return "button"

@pytest.fixture()
def selector_button_create_post():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def selector_input_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def selector_input_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def selector_input_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def selector_save_button():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""



@pytest.fixture()
def selector_return_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def selector_return_error():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def selector_return_home():
    return """//*[@id="app"]/main/nav/a/span"""

@pytest.fixture()
def site():
    site_instance = Site(testdata.get('address'))
    yield site_instance
    site_instance.my_quit()
