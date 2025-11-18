from __future__ import annotations
from SpineSegment import SpineSegment


class Spine:
    def __init__(self, id: int, spine_segments: list[SpineSegment]) -> None:
        self.id = id
        self.spine_segs = spine_segments
        self.quality = self._determine_quality()

    def _determine_quality(self):
        quality_string = ""
        for seg in self.spine_segs:
            quality_string += str(seg.middle)
        quality = int(quality_string)
        return quality

    @property
    def get_quality(self):
        return self.quality

    def compare_segments(self, other: Spine) -> int:
        lesser = min(len(self.spine_segs), len(other.spine_segs))

        for i in range(lesser):
            if self.spine_segs[i].quality > other.spine_segs[i].quality:
                return -1
            elif self.spine_segs[i].quality < other.spine_segs[i].quality:
                return 1

        # If they are identical, instead use the ID for comparison
        if self.id < other.id:
            return 1
        elif self.id > other.id:
            return -1
        raise Exception

    def __repr__(self):
        return f'{self.id}'
