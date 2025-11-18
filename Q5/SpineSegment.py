class SpineSegment:
    def __init__(self, first_element: int, on_init) -> None:
        self.left = None
        self.right = None
        self.middle = first_element
        self._on_init = on_init
        self._on_init(self)
        self._completed = False  # prevents double-calling

    @property
    def is_complete(self) -> bool:
        return (
            self.left is not None and
            self.right is not None and
            self.middle is not None
        )

    def add_element(self, new_element: int) -> bool:
        added = False
        if new_element < self.middle and not self.left:
            self.left = new_element
            added = True
        elif new_element > self.middle and not self.right:
            self.right = new_element
            added = True
        else:
            added = False
        return added

    @property
    def quality(self) -> int:
        seg_string = ""
        if self.left:
            seg_string += str(self.left)
        if self.middle:
            seg_string += str(self.middle)
        if self.right:
            seg_string += str(self.right)
        return int(seg_string)

    def __repr__(self) -> str:
        string = ""
        if self.left:
            string += f'{self.left}-'
        else:
            string += '  '
        if self.middle:
            string += f'{self.middle}'
        if self.right:
            string += f'-{self.right}'
        return string
