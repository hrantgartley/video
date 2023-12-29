from movie import Movie


class Actor(Movie):
    def __init__(self, age: int, num_movie: int) -> None:
        self.age = age
        self.num_movie = num_movie

    def __str__(self) -> str:
        return (
            f"Actor age: {self.age}"
            f"Number of movies: {self.num_movie}"
        )
