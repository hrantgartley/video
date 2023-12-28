import random

from video_class import Video


def print_msg(msg) -> None:
    print(f"The given message was {msg}")


def bound(lower, upper) -> int:
    return random.randint(lower, upper)


def main():
    video1 = Video(True, 120, [], 4.5)
    video2 = Video(False, 60, ["comedy", "action"], 3.5)
    video3 = Video(True, 90, ["drama"], 5.0)
    video_list = [video1, video2, video3]
    for _ in range(len(video_list)):
        print(video_list)

    for key, value in enumerate(video_list):
        print("key:", key, "value:", value)


if __name__ == "__main__":
    main()
