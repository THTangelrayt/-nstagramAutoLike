from selenium import webdriver
import time

cx= "İlk 7 kullanıcın resmini beğenebilirsiniz"
print(cx)

kadi=input("Kullanıcı adınızı giriniz")
passw=input("Şifrenizi giriniz")

print("Kullanıcı adınız :" +kadi)
print("Şifreniz         :" +passw)
print("Olarak ayarlanmıştır")


onay = input("Giriş yaptıktan sonra otomatik olarak beğenmek istermisiniz ?  y/n ")




browser = webdriver.Firefox()
#
browser.get("https://instagram.com")
time.sleep(3)
giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")


giris_yap.click()
time.sleep(2)

username = browser.find_element_by_name(kadi)
password = browser.find_element_by_name(passw)
username.send_keys("kullanıcı adınız")
password.send_keys("şifreniz")

sisteme_gir = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button")
sisteme_gir.click()

time.sleep(4)


begen0 =browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[1]/div/article[1]/div[2]/section[1]/a[1]/span")

begen0.click()

begen =browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[1]/div/article[2]/div[2]/section[1]/a[1]/span")

begen.click()
begen2 =browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[1]/div/article[3]/div[2]/section[1]/a[1]/span")

begen2.click()
begen3 =browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[1]/div/article[4]/div[2]/section[1]/a[1]/span")

begen3.click()
begen4 =browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[1]/div/article[5]/div[2]/section[1]/a[1]/span")

begen4.click()
begen5 =browser.find_element_by_xpath("//*[@id='react-root']/section/main/section/div/div[1]/div/article[6]/div[2]/section[1]/a[1]/span")

begen5.click()




    


    


time.sleep(50)
a = input("Çıkmak için bir tuşa basınız")
print(a)


browser.close()
