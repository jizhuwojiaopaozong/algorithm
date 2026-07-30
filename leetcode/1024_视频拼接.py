from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: x[0])
        if not clips:
            return 0
        res = 0
        last = 0
        i = 0
        while i < len(clips):
            if clips[i][0] > last:
                return -1
            tmp = 0
            while i < len(clips) and clips[i][0] <= last:
                tmp = max(tmp, clips[i][1])
                i += 1
            last = tmp
            res += 1
            if last >= time:
                break
        if last >= time:
            return res
        else:
            return -1
