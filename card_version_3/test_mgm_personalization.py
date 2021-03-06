from time import sleep


from model import unit_init
from utils.url import CardUrl
from web.login_operator import LoginOperator


class MgmPersonalizationTest(unit_init.Base):

    def login(self, url):
        LoginOperator(self.driver).mgm_recommendation_login("17621523736", "李孝雪", url, 1001)
        sleep(1)

    # mgm选择卡种按钮
    def test_select_mgm_custom_recommend(self):
        self.login(CardUrl.MGM_PERSONALIZATION_URL)
        LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[3]/div/label'))
        sleep(120)
        # message = self.driver.find_element_by_xpath('/html/body/div/div[1]').text
        # self.assertIn(u'客户参与活动，推荐达标后即可自动领取奖品', message)

    # TODO 通过class是否checked判断选择卡种和排除卡种
    # mgm排除卡种按钮
    def test_exclude_mgm_custom_recommend(self):
        self.login(CardUrl.MGM_PERSONALIZATION_URL)
        LoginOperator(self.driver).click((By.XPATH, '//*[@id="app"]/div/ul/li[1]/div/div[4]/div/label'))
        sleep(2)

