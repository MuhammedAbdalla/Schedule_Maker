from bs4 import BeautifulSoup
import logging
import requests
import threading
import time

DEPARTMENTS = ["biomedical-engineering","electrical-computer-engineering","engineering-core","mechanical-engineering"]
DEP_NAMES = ["Biomedical Eng", "Electrical & Computer Eng", "Eng Core", "Mechanical Eng"]


classlist = list()


def scrapeClasses(department, core: str = "1"):
    url = "https://www.bu.edu/academics/eng/courses/" + department
    result1 = requests.get(url)
    classhtml1 = BeautifulSoup(result1.text, "html.parser")
    
    nums = classhtml1.find(class_ = "pagination").find_all("a")
    pages = int(nums[nums.__len__()-1].string)

    print("There are {p} pages of BU {c} courses".format(p = pages, c = DEP_NAMES[core]))

    for page in range(pages):
        resultN = requests.get(url + "/" + str(page))
        classhtmlN = BeautifulSoup(resultN.text, "html.parser")
        classesN = classhtmlN.find_all("strong")
        for i in classesN:
            if i.string[0] == 'E' and i.string[1] == 'N' and i.string[2] == 'G':
                if (not classlist.__contains__(i.string)):
                    classlist.append(i.string)
                #print("--- Core {c}: {s}".format(c=core, s=i.string))


def scrapeDetails(course):
    url = "https://www.bu.edu/academics/eng/courses/" + ("-".join(course.split(" "))).lower()
    result = requests.get(url)
    classhtml = BeautifulSoup(result.text, "html.parser")
    #return classhtml.prettify()
    cf_course = classhtml.find(class_ = "cf-course").find_all(["strong","td"])
    sections = list()
    details = list()
    count = 1
    with open("Schedule.txt", "w") as sfile:
        for tag in cf_course:
            details.append(tag.string)
            count += 1
            if (count % 7 == 0):
                count = 1
                print(details)
                sections.append(details)
                #sfile.write(", ".join(details))
                details = list()
                details.append(course)
    return sections



def getClasses():
    logging.info("Scrape Start")
    for i, d in enumerate(DEPARTMENTS):
        scrapeClasses(department=d,core=i)
    logging.info("Scrape Finish")


def getClasses_T():
    threads = list()

    for i, d in enumerate(DEPARTMENTS):
        x = threading.Thread(target = scrapeClasses, args = (d,i), daemon=False)
        threads.append(x)
        x.start()

    for thread in threads:
        thread.join()

    with open("courses.txt", "w") as f1:
        classlist.sort()
        for c in classlist:
            f1.write(c+'\n')


def getHTML():
    url = "https://www.bu.edu/academics/eng/courses/"
    result_t = requests.get(url)
    html_t = BeautifulSoup(result_t.text, "html.parser")
    with open("courses.html", "w") as file:
        file.write(html_t.prettify())
    print("HTML printed")


def scraper1():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO,datefmt="%H:%M:%S")
    logging.info("Threaded Scrape Start")
    getClasses_T()
    logging.info("Threaded Scrape Finish")


def scraper2():    
    with open("courses.txt","r") as file:
            for i, line in enumerate(file.readlines()):
                scrapeDetails(line.split(":")[0])
                

def scraper3():    
    scrapeDetails("ENG EC 440")

if __name__ == "__main__":
    #format = "%(asctime)s: %(message)s"
    #logging.basicConfig(format=format, level = logging.INFO,datefmt="%H:%M:%S")
    #getClasses()
    #getClasses_T()
    getHTML();