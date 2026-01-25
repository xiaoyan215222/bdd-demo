import logging
import sys
from time import sleep
from selenium import webdriver
from behave import given,when,then
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#模拟全局变量，存储测试数据
text_context={
    "username":"",
    "password":""
}
@given("系统已启动，且登录页面可以访问")
def step_impl(context):
    if sys.platform=='win32':
        context.driver=webdriver.Chrome()
    else:
        # 配置Chrome/Chromium选项（适配GitHub Actions无煮面环境）
        chrome_options = Options()
        # 核心参数：无头模式+突破Ubuntu沙箱限制（必加）
        chrome_options.add_argument("--headless=new")  # 新版无头模式，兼容性最好
        chrome_options.add_argument("--no-sandbox")  # 禁用Ubuntu权限沙箱问题（关键!)
        chrome_options.add_argument("--disable-dev-shm-usage")  # 解决CI内存不足
        chrome_options.add_argument("--disable-gpu")  # 禁用gpu(无头模式不需要”）
        chrome_options.add_argument("--remote-debugging-port=9222")  # 兼容无头模式启动
        # 2.显式指定chromium二进制文件路径（匹配CI环境的安装配置）
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        # 3.显示指定ChromeDriver路径（匹配CI环境的驱动路径）
        chrome_service = Service(executable_path="/usr/bin/chromedriver")
    # 4初始化驱动（指定service和options,而非空参数）
    try:
        context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    except Exception as e:
        print(f"Chrome驱动初始化失败:{str(e)}")
        raise
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

