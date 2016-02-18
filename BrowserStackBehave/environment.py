from selenium import webdriver

def before_all(context):
  desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
  desired_capabilities['platform'] = 'WINDOWS'

  context.browser = webdriver.Remote(
    desired_capabilities=desired_capabilities,
    command_executor="http://colinmoorehill1:S3pkYYSJkVR5GcpTxvTY@hub.browserstack.com:80/wd/hub"
  )

def after_all(context):
  context.browser.quit()