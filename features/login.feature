Feature:用户登录功能
  作为用户，我希望通过正确的账号密码登录系统，错误信息能正确提示

  @smoke
  Scenario:用户正常登录
    Given 系统已启动，且登录页面可以访问
    When  输入正确用户名和正确密码
    And   点击登录
    Then  登录成功


  Scenario:密码错误，提示用户名或者密码错误
    Given 系统已启动，且登录页面可以访问
    When  输入正确用户名和错误密码
    And   点击登录
    Then  登录失败