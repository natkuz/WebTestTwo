import yaml
# from module import Site
import pytest
import time

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

# site = Site(testdata.get('address'))

def test_step_one(site, selector_input_login, selector_input_password, selector_button, selector_return_error):
    input_one = site.find_element('xpath', selector_input_login)
    input_one.send_keys('test')
    input_two = site.find_element('xpath', selector_input_password)
    input_two.send_keys('test')
    button = site.find_element("css", selector_button)
    button.click()
    err_label = site.find_element('xpath', selector_return_error)
    assert err_label.text == "401", "test_step_one FAILED"


def test_step_two(site, selector_input_login, selector_input_password, selector_button, selector_return_home):
    input_one = site.find_element('xpath', selector_input_login)
    input_one.send_keys(testdata.get('login'))
    input_two = site.find_element('xpath', selector_input_password)
    input_two.send_keys(testdata.get('password'))
    button = site.find_element("css", selector_button)
    button.click()
    label = site.find_element('xpath', selector_return_home)
    assert label.text == "Home", "test_step_two FAILED"


def test_step_three(site, selector_input_login, selector_input_password, selector_button,
                    selector_button_create_post, selector_input_title, selector_input_description,
                    selector_input_content, selector_save_button, selector_return_title):
    input_one = site.find_element('xpath', selector_input_login)
    input_one.send_keys(testdata.get('login'))
    input_two = site.find_element('xpath', selector_input_password)
    input_two.send_keys(testdata.get('password'))
    button = site.find_element("css", selector_button)
    button.click()
    time.sleep(testdata.get('sleep_time'))
    create_button = site.find_element('xpath', selector_button_create_post)
    create_button.click()
    time.sleep(testdata.get('sleep_time'))
    input_title = site.find_element('xpath', selector_input_title)
    input_title.send_keys(testdata.get('title'))
    input_description = site.find_element('xpath', selector_input_description)
    input_description.send_keys(testdata.get('description'))
    input_content = site.find_element('xpath', selector_input_content)
    input_content.send_keys(testdata.get('content'))
    time.sleep(testdata.get('sleep_time'))
    button_save = site.find_element('xpath', selector_save_button)
    button_save.click()
    time.sleep(testdata.get('sleep_time'))
    title = site.find_element('xpath', selector_return_title)
    assert title.text == testdata.get('title'), "test_step_three FAILED"


if __name__ == '__main__':
    pytest.main(['-vv'])