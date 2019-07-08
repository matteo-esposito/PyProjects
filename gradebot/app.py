from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import base64
import getpass
import sys


class GradeBot():
    def __init__(self, username, password):
        """Gradebot! Your automated MyConcordia grade checker. For those stressful times
        where you are obsessively checking your grades that always seem to come out way later than expected :P
        
        Arguments:
            username {string} -- MyConcordia username
            password {string} -- MyConcordia password
        """
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        # Goto site
        bot = self.bot
        bot.get("https://my.concordia.ca/psp/upprpr9/?cmd=login&languageCd=ENG")
        time.sleep(3)

        # Locate and populate user and pwd fields.
        user_field = bot.find_element_by_class_name('form_login_username')
        pwd_field = bot.find_element_by_class_name('form_login_password')
        user_field.clear()
        pwd_field.clear()
        user_field.send_keys(self.username)
        pwd_field.send_keys(self.password)
        pwd_field.send_keys(Keys.RETURN)
        time.sleep(10)

        # Goto student center and find grades
        bot.find_element_by_xpath('//a[@id="fldra_CU_MY_STUD_CENTRE" and @class="ptntop"]').click()
        time.sleep(1.5)
        bot.find_element_by_xpath('//a[@class="ptntop" and @role="menuitem" and @href="https://my.concordia.ca/psp/upprpr9/EMPLOYEE/EMPL/s/WEBLIB_CONCORD.CU_SIS_INFO.FieldFormula.IScript_Campus_Student_Trans?FolderPath=PORTAL_ROOT_OBJECT.CU_MY_STUD_CENTRE.CAMPUS_STUDENT_TRANSCRIPT&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder"]').click()
        # time.sleep(7)
        # bot.find_element_by_xpath("//input[@name='SSR_DUMMY_RECV1$sels$0'][@type='radio']").click()
        time.sleep(3)
        bot.find_element_by_xpath('//span[@class="PSPUSHBUTTON" and @name="DERIVED_SSS_SCT_SSR_PB_GO"]').click()
        

if __name__ == '__main__':
    # user = input('Username: ')
    # pwd = getpass.getpass()
    # checker = GradeBot(user, pwd)
    f = open("userinfo.txt", "r")
    pwd = f.read()
    print(pwd)
    # checker = GradeBot('M_ES', str(pwd))
    # checker.login()