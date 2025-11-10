from sympy import false

from src.bowling_error import  BowlingError
from src.frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames =[]

    def add_frame(self, frame: Frame) -> None:
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self._frames):
            raise BowlingError
        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
        for i, frame in enumerate(self._frames):
            if frame.is_spare():
                self.bonus_spare(i, frame, len(self._frames))
            elif frame.is_strike():
                self.bonus_strike(i, frame, len(self._frames))

            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self._bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self._second_bonus_throw = bonus_throw

    def bonus_spare(self, i: int, frame: Frame, total_frames: int) -> None:
        is_last_frame = (i == total_frames - 1)
        if is_last_frame:
            frame.set_bonus(self._bonus_throw)
        else:
            frame.set_bonus(self._frames[i + 1].get_first_throw())

    def bonus_strike(self, i: int, frame: Frame, total_frames: int) -> None:
        is_last_frame = (i == total_frames - 1)
        is_second_to_last_frame = (i == total_frames - 2)
        if is_last_frame:
            frame.set_bonus(self._bonus_throw + self._second_bonus_throw)
        elif is_second_to_last_frame:
            next_frame = self._frames[i + 1]
            frame.set_bonus(next_frame.get_first_throw() + self._bonus_throw)
        else:
            next_frame = self._frames[i + 1]
            if next_frame.is_strike():
                frame_after_next = self._frames[i + 2]
                bonus = next_frame.get_first_throw() + frame_after_next.get_first_throw()
                frame.set_bonus(bonus)
            else:
                bonus = next_frame.get_first_throw() + next_frame.get_second_throw()
                frame.set_bonus(bonus)
