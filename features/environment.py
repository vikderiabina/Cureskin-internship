from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    service = Service(executable_path=r'C:\Users\vderiabina\PycharmProjects\Cureskin-internship\chromedriver.exe')
    # context.driver = webdriver.Chrome(service=service)


    # context.driver = webdriver.Firefox(
    #     executable_path=r'C:\Users\vderiabina\PycharmProjects\Cureskin-internship\geckodriver')

    ###### HEADLESS MODE #############
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable')
    chrome_options.add_argument("--window-size=1920,1080")

    context.driver = webdriver.Chrome(
        chrome_options=chrome_options,
        service=service
    )

    # ### BROWSERSTACK ####
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     'name': test_name
    # }
    # bs_user = 'victoriaderiabin_pSlLsE'
    # bs_key = 'eB2fiuLoesvgPeNpyeSK'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.maximize_window()
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        # logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
