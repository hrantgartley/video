import random
import re
from typing import Tuple

import requests
from requests import exceptions, get


class Video:
    def __init__(self, is_watchable: bool = False, length: int = 0,
                 watch_list: list = [], rating: float = 0):
        self.is_watchable = is_watchable
        self.length = length
        self.watch_list = watch_list
        self.rating = rating
        self.names = []

    def __str__(self):
        return (
            f"Name: {self.read_from_file()}\n"
            f"Video length: {self.length}\n"
            f"Is it watchable: {self.is_watchable}\n"
            f"Rating: {self.rating}\n"
        )

    def get_rating(self):
        return self.rating

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_watchlist(self):
        return self.watch_list

    def add_to_watchable_list(self, item):
        return self.watch_list.append(item)

    def find_error(self):
        return "is this manageable??"

    def print_error(self, msg):
        print(f"{msg} could not be added to the list")

    def print_success(self, msg):
        print(f"{msg} added to the list")

    def define_watchable(self, item_to_add):
        if self.length > 20 and self.rating > 3.5:
            self.watch_list.append(item_to_add)
            self.print_success(item_to_add)
            return
        else:
            self.print_error(item_to_add)
            return

    def read_from_file(self):
        try:
            with open("names.txt", "r") as file:
                for line in file.readlines():
                    capitalized_line = line.strip().capitalize()
                    print(capitalized_line)
        except FileNotFoundError as err:
            print(err)

    def write_to_file(self, filename, msg):
        with open(filename, "w") as file:
            if msg == "" or msg == " ":
                return
            elif msg is None:
                return
            else:
                file.write(msg)

    def file_append(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                capitalize_first_letter: str = line.strip().capitalize()
                self.names.append(capitalize_first_letter)
        return random.choice(self.names)

    def array_append(self) -> Tuple[bool, str]:
        try:
            with open("names.txt", "r") as f:
                lines = f.readlines()
            with open("names.txt", "w") as f:
                for line in lines:
                    f.write(line)
            return True, "File contents appended"

        except FileNotFoundError:
            return False, "File could not be found"

    def return_random_name(self):
        return random.choice(self.names)

    def read_num_names(self, bound):
        try:
            with open("names.txt", "r") as f:
                lines = f.readlines()
                for line in lines[:bound]:
                    print(line.strip().capitalize())
        except FileNotFoundError as err:
            print(err)
        finally:
            print("Execution complete")

    def valid_name(self, name):
        pattern = re.compile(r"^[A-Za-z]+$")
        if pattern.match(name):
            return True
        else:
            return False

    def watch_count(self):
        good = self.is_watchable
        if good:
            self.is_watchable += 1
        return good

    def add_video(self, is_watchable: bool = False, length: int = 0, watch_list: list = [], rating: float = 0):
        new_video = Video(is_watchable, length, watch_list, rating)
        return new_video

    def remove_video(self, genre):
        for iter, video in enumerate(self.watch_list):
            if video.genre == genre:
                self.watch_list.remove(iter)
        return

    def backup_print(self, videos: list):
        for i, video in enumerate(videos):
            print(f"Video {i+ 1}\n {video}")
        return

    def ping_video(self, url):
        try:
            response = get(url)
            return response.status_code
        except exceptions.ConnectionError:
            return "Connection Error"

    def get_vid_id(self, url):
        yt_id = r"/(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^\"&?\/\s]{11})/gi"
        match = re.match(yt_id, url)
        if match:
            return match.group(1)
        return False

    def num_comments(self, url):
        if self.is_watchable:
            return url.all_comments()
        else:
            return requests.ConnectionError()
