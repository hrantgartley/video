from video_class import Video


class Movie(Video):
    def __init__(self, is_watchable: bool = False, length: int = 0,
                 watch_list: list = [], rating: float = 0):
        super().__init__(is_watchable, length, watch_list, rating)
        self.genre = ""
        self.title = ""
        self.director = ""
        self.actors = []
        self.release_date = ""

    def __str__(self):
        return (
            f"Name: {self.title}\n"
            f"Video length: {self.length}\n"
            f"Is it watchable: {self.is_watchable}\n"
            f"Rating: {self.rating}\n"
            f"Genre: {self.genre}\n"
            f"Director: {self.director}\n"
            f"Actors: {self.actors}\n"
            f"Release date: {self.release_date}\n"
        )

    def show_list(self):
        for index, v in enumerate(self.watch_list):
            if self.watch_list[index] == '':
                continue
            print("values:", v)

    def show_actors(self):
        for index, v in enumerate(self.actors):
            print(f"Actor{index+1}: {self.actors[v]}")

    def find_error(self):
        return super().find_error()
