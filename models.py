class SinhVien:
    def __init__(self, mssv, ho_ten, nganh_hoc, id=None):
        self.id = id
        self.mssv = mssv
        self.ho_ten = ho_ten
        self.nganh_hoc = nganh_hoc

    def __str__(self):
        return f"[{self.id}] {self.mssv} - {self.ho_ten} - {self.nganh_hoc}"