import logging
from time import sleep
from selenium import webdriver
from behave import given,when,then
from selenium.webdriver.common.by import By

#模拟全局变量，存储测试数据
text_context={
    "username":"",
    "password":""
}
@given("系统已启动，且登录页面可以访问")
def step_impl(context):
    context.driver=webdriver.Chrome()
    context.driver.get("https://eaton-sc-web.houyuzhu.com.cn:81/#/login")
    sleep(3)


@when("输入正确用户名和正确密码")
def step_impl(context):
    context.driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名"]').send_keys("xiaoyan")
    context.driver.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys("xiaoyan")

@when("输入正确用户名和错误密码")
def step_impl(context):
    context.driver.find_element(By.XPATH, '//input[@placeholder="请输入用户名"]').send_keys("xiaoyan")
    context.driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys("xiaoyanA")



@when("点击登录")
def step_impl(context):
    context.driver.find_element(By.XPATH, '//button[@type="button"]').click()


@then("登录成功")
def step_impl(context):
    sleep(3)
    url=context.driver.current_url
    logging.info(msg=f"返回url为修改{url}")
    assert url=='https://eaton-sc-web.houyuzhu.com.cn:81/#/models'

@then("登录失败")
def step_impl(context):
    logging.info("登录失败，请重新登录")
    assert context.driver.current_url =="https://eaton-sc-web.houyuzhu.com.cn:81/#/login"

