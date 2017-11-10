'''
fxiao自动写日志
++++++++++++++++++++
1. 测试异常
2. 定时发送
3. 完全后台运行在session0，设定显式/隐式等待防止渲染失败
*4. 机器学习/监督学习/隐马尔可夫模型-日志内容
5. 生成系统日志

update:
v1.0 beta 已实现伪随机文本生成
+++++++++++++++++++

'''


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import generate_text as gt


def set_options():
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"')
    options.add_argument('--headless')
    #options.add_argument('--ssl-protocol=any') 改变协议
    options.add_argument('--disable-gpu')
    
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(30) #非常关键，后台加载极有可能渲染失败
    browser.maximize_window()
    browser.get('https://www.fxiaoke.com/XV/Home/Index#stream')

    return browser

def login(browser):
    browser.find_element_by_xpath('//div[@class="fx-tabs login-tabs"]/div[2]').click()
    browser.find_element_by_xpath('//input[@class="fx-ipt j-ipt-phone-num ipt-phone-num"]').send_keys("18911669199")
    browser.find_element_by_xpath('//input[@class="fx-ipt j-ipt-password ipt-password"]').send_keys("123456whw")
    browser.find_element_by_xpath('//div[@class="fx-form-control j-btn-login btn-login"]/div').click()


def write(browser):
    browser.find_element_by_xpath('//li[@class="fs-publish-nav j-tab-plan ui-tab-item ui-switchable-trigger"]/a').click()
    browser.find_element_by_xpath('//textarea[@data-autolistid="fs-publish-2"]').send_keys(gt.today())
    #browser.find_element_by_css_selector("textarea").send_keys("数据分析，测试新的功能")
    browser.find_element_by_xpath('//textarea[@data-autolistid="fs-publish-3"]').send_keys(gt.tmr())
    browser.find_element_by_xpath('//*[@id="w_page_container"]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[1]/div[1]/div[1]/fieldset[3]/textarea').send_keys(gt.exp())
    browser.find_element_by_xpath('//*[@id="w_page_container"]/div[2]/div[1]/div/div[2]/div[2]/div/form/div[5]/div[3]/button').submit()
    time.sleep(3) #必须存在，否则报错
    #ActionChains().double_click(btn).perform() 

def main():
    logs=['\n\n']
    logs.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    try:
        browser = set_options()
        logs.append('\n\toptions finished')
        #page = browser.page_source
        login(browser)
        logs.append('\n\tlogin finished')
        write(browser)
        logs.append('\n\twrite finished')
        browser.quit()
    except Exception as e:
        logs.append('\tError')
    finally:      
        with open("C:\\Users\\tcsd\\Desktop\\MyDataWork\\daily_diary\\logs.txt",'a') as f:
            for elog in logs:
                f.writelines(elog)
                print('\n')
    

if __name__ == "__main__":
    main()
    
'''隐式等待
    try:
        wait = WebDriverWait(browser,15).until(
            EC.visiblity_of_element_located((By.data-autolistid, "fs-publish-2"))

        )
    except Exception as e:
        print("页面渲染失败！")
        write(browser)
    else:
'''
''' Linux下实现静默运行，win不支持xvfb
    try:
    display =Display(backend="xvfb",visible=0, size=(1366,768))
    display.start()
    display.stop()
'''

    
