# 补充：场景结束后关闭浏览器，避免资源泄露
def after_scenario(context, scenario):
    """每个场景执行完后关闭浏览器"""
    if hasattr(context, 'driver'):
        context.driver.quit()