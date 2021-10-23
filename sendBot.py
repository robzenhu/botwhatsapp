from selenium import webdriver
import time


class botwhatsapp:
    def __init__(self):
        self.messenge = "I'm testing a bot" #the message you want to send
        self.send_to_groups = ["Group1","Group2","Group3"] #Name of the groups or people you want to send the message to
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver=webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=options)    
    
    def Send_messages(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)
        for groups in self.send_to_groups:
            time.sleep(10)   
            search =  self.driver.find_element_by_xpath(f"//span[@title='{groups}']")
            time.sleep(3)
            search.click()
            time.sleep(3)
            #write the message
            messenger_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            messenger_box.click()
            messenger_box.send_keys(self.messenge) 
            #click the send button 
            to_send = self.driver.find_element_by_xpath("//div[@class='_3HQNh _1Ae7k']")
            time.sleep(3)
            to_send.click()
            time.sleep(2)

bot = botwhatsapp()
bot.Send_messages()
            
            
        