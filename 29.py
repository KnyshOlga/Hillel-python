class Counter:
    def __init__(self, min_=0, max_=10, current=1):
        self._min = min_
        self._max = max_
        self._current = current

    def get_current(self):
        return self._current

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def set_current(self, current):
        self._current = current

    def set_max(self, max_):
        self._max = max_

    def set_min(self, min_):
        self._min = min_

    def step_down(self):
        if self._current - 1 < self._min:
            raise ValueError('Minimum value exceeded')
        self._current -= 1

    def step_up(self):
        if self._current + 1 > self._max:
            raise ValueError('Maximum value exceeded')
        self._current += 1


counter = Counter()

assert counter.get_min() == 0, 'Initial minimum value is invalid'
assert counter.get_max() == 10, 'Initial maximum value is invalid'
assert counter.get_current() == 1, 'Initial current value is invalid'

counter.set_current(7)
assert counter.get_current() == 7, 'Current value is invalid'

counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10

try:
    counter.step_up()
except ValueError as e:
    assert str(e) == 'Maximum value exceeded'
    assert counter.get_current() == counter.get_max() == 10, 'Current value changed'

counter.set_min(7)
assert counter.get_min() == 7, 'Minimum value is invalid'
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Current value is invalid'

try:
    counter.step_down()
except ValueError as e:
    assert str(e) == 'Minimum value exceeded'
    assert counter.get_current() == counter.get_min() == 7, 'Current value changed'
