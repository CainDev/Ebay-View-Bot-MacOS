from random import *
from time import sleep
import requests as bot

# Globals
program_running = True
program_warning_bool = False

view_delay_set = False
view_delay_enabled = False
view_next_step = False
view_delay_time = 0
view_delay_random = False

ebay_urls_set = False
ebay_urls = []
ebay_views = []


def skip_warning():
    global program_warning_bool
    with open("settings.txt", "r") as settings:
        file_information = settings.readlines()
        for line in file_information:
            if line.lower().__contains__("skip-warning=true"):
                program_warning_bool = True
                break
            elif line.lower().__contains__("skip-warning=false"):
                program_warning_bool = False
                break
    settings.close()


def send_views(ebay_url, ebay_view_count):
    current_views = 0
    seed(3790579)

    while current_views < int(ebay_view_count):
        if current_views != int(ebay_view_count):
            if view_delay_enabled:
                sleep(view_delay_time)
                print("Slept for " + str(view_delay_time) + " Seconds...")
            elif view_delay_random:
                random_sleep = randint(1, 10)
                sleep(random_sleep)
                print("Slept for " + str(random_sleep) + " Seconds...")

        bot.get(ebay_url)
        current_views = current_views + 1
        print("View " + str(current_views) + " Sent Successfully to " + str(ebay_url))


def program_warning():
    print("There is very little verification checks. So make sure you are responding properly to the questions.")
    print("Aka if it says Y/N only respond Y or N. Also when it asks for Views provide a NUMBER ONLY.")
    print("Contact Timothyy#6466 on Discord for Help if required.")
    print("Press any key to continue....")
    input()


def define_view_delay():
    global view_next_step
    global view_delay_enabled
    user_response = ""
    print("Do you want to enable View Delay? [Y/N]")
    user_response = input()

    if user_response.lower() == "y":
        view_next_step = True
    else:
        view_next_step = False


def set_view_delay():
    global view_delay_time
    global view_delay_random
    global view_delay_enabled
    user_response = 0
    print("How long do you want the delay to be? (In Seconds, 1 - 10, 0 for Randomised)")
    user_response = input()

    if int(user_response) == 0:
        view_delay_random = True
    elif int(user_response) > 10 | int(user_response) < 1:
        print("Please 1 - 10 Seconds only please.")
        set_view_delay()
    else:
        view_delay_enabled = True
        view_delay_time = int(user_response)
        print("Delay set to " + str(view_delay_time) + " Seconds.")


def add_ebay_urls():
    global ebay_urls
    global ebay_views
    global ebay_urls_set
    user_response = 0
    link_count = 0

    print("How many products do you want to boost?")
    user_response = input().strip()

    if int(user_response) >= 1:
        while link_count < int(user_response):
            print("What is the URL for Product " + "{" + str(link_count) + "}")
            ebay_urls.append(input().strip())
            print("How many Views for Product " + "{" + str(link_count) + "}")
            ebay_views.append(input().strip())
            link_count = link_count + 1
    else:
        print("Please try again.")
        add_ebay_urls()

    ebay_urls_set = True


def main_script():
    global program_warning_bool
    global program_running

    if not program_warning_bool:
        program_warning()
        program_warning_bool = True

    define_view_delay()
    if view_next_step:
        set_view_delay()

    if not ebay_urls_set:
        add_ebay_urls()

    if ebay_urls_set:
        current_count = 0
        for link in ebay_urls:
            send_views(link, ebay_views[current_count])
            current_count = current_count + 1

    program_running = False


while program_running:
    if not program_warning_bool:
        skip_warning()
    main_script()
