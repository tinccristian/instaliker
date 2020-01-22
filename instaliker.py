from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import getpass
def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(5)

            
    def like_photo(self,hashtag,prange,waiter):

        count=0
        driver = self.driver        
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]').click()                          #latest photo
        time.sleep(2)

        copy=waiter
        for  i in range(prange):                                                                                                         #like first prange photos
            try:
                try:
                    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()        #like photo
                except:
                        try:
                            driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/section[1]/span[1]').click()
                        except:
                            print("\n100 failed to find like button twice, going to the next photo")
                            try:
                                driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
                            except:
                                print("\n101 failed to go to the next photo. fix the script. Maybe just try running again?")
                try:        
                    count+=1
                    for second in reversed(range(0, random.randint(int(0.75*copy),int(1.25*copy)))):
                        if count==1 and second!=0:
                            print_same_line(str(count) + ' photo liked from # '  + str(hashtag)   + " | waiting "  + str(second) +" seconds.        " )
                            time.sleep(1)
                        elif second!=0:
                            print_same_line(str(count) + ' photos liked from # '  + str(hashtag)   + " | waiting "  + str(second) +" seconds.       " )
                            time.sleep(1)
                        elif count<prange:
                            print_same_line(str(count) + ' photos liked from # '  + str(hashtag)   + " | going to the next one ... "  )
                            time.sleep(1)
                        else:
                            print_same_line("            " +str(count) + ' photos liked from # '  + str(hashtag)   + ".            " )
                except :
                    print("\n103 failed to display data, program probably still works, check if you can, no need to worry")
                try: 
                    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()                                                #go to next photo
                    time.sleep(2)
                except:
                    print("\n104 failed to go to the next photo. fix the script. Maybe just try running again?")
            except :
                print("\n105 failed to like a photo after a lot of attempts.")
                time.sleep(3)
                driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()                   #go next photo
        print("\n_____________________________________________________\n" )
        




if __name__ == "__main__":
    hashtags=[]
    username = str(input("Username: "))
    password = getpass.getpass()
    number=int(input("How many hashtags to loop through? "))
    for i in range(number):
        hashtags.append(str(input("Hashtag "+str(i+1)+": ")))
    prange=int(input("How many pictures to like from each hashtag? "))
    waiter=int(input("How many seconds to wait between each like?(18 gives 200 likes/ hour): "))
    print("Opening the browser...")
    ig = InstagramBot(username, password)
    print("Logging in to "+str(username)+"...")
    ig.login()

    print("picking a random hashtag...\n" )
    print("_____________________________________________________\n" )

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            print_same_line("               going to #" +tag)
            ig.like_photo(tag,prange,waiter)
        except:
            try:
                print("\n106 bot crashed, going to next tag")
                tag = random.choice(hashtags)
                print_same_line("               going to #" +tag)
                ig.like_photo(tag,prange,waiter)
            except :
                print("\n107 bot seriously crashed, restarting after 60 s. Most likely tags are bad")
                ig.closeBrowser()
                time.sleep(60)
                ig = InstagramBot(username, password)
                ig.login()

    



            