class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.arr = {}
        self.snap_map = {}
        self.count = 0
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.count += 1
        self.snap_id = self.count - 1
        self.snap_map[self.snap_id] = self.arr.copy()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snap_map:
            d_at_snap = self.snap_map[snap_id]
            if index in d_at_snap:
                return d_at_snap[index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)