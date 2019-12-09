from bank.test.models import myunit
from bank.login.login import Login
from bank.test.car_payment.car_payment_second import CarPaymentPersonalInfo

from time import sleep

from bank.test.page_obj.base_info_test import DetailInfoTest
from bank.test.page_obj.base_info import BaseInfo

class CarPaymentPersonalTest(myunit.MyTest):

    def car_payment_personal_page(self, company, salary, url):
        # url = 'https://test.xliane.com/html2/webapp/fastIssue/index.html#/mgm/index'
        CarPaymentPersonalInfo(self.driver).car_payment_personal_info(company, salary, url)



    def test_car_paymentinfo(self):
        url = 'https://test.xliane.com/html2/car-instalment3/second.html'
        self.car_payment_personal_page("上海科技馆", 110, url)




