from abc import ABC, abstractmethod
from models import SinhVien

class BaseRepository(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, entity_id):
        pass

    @abstractmethod
    def delete_by_id(self, entity_id):
        pass

class SinhVienRepository(BaseRepository):
    def __init__(self, db):
        self.db = db

    def save(self, sv):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO sinh_vien (mssv, ho_ten, nganh_hoc) VALUES (%s, %s, %s)"
        val = (sv.mssv, sv.ho_ten, sv.nganh_hoc)
        cursor.execute(sql, val)
        conn.commit()
        sv.id = cursor.lastrowid
        cursor.close()
        conn.close()
        return sv.id

    def update(self, sv):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "UPDATE sinh_vien SET mssv = %s, ho_ten = %s, nganh_hoc = %s WHERE id = %s"
        val = (sv.mssv, sv.ho_ten, sv.nganh_hoc, sv.id)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def find_all(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sinh_vien")
        rows = cursor.fetchall()
        danh_sach = []
        for row in rows:
            sv = SinhVien(row['mssv'], row['ho_ten'], row['nganh_hoc'], row['id'])
            danh_sach.append(sv)
        cursor.close()
        conn.close()
        return danh_sach

    def find_by_id(self, sv_id):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM sinh_vien WHERE id = %s"
        cursor.execute(sql, (sv_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return SinhVien(row['mssv'], row['ho_ten'], row['nganh_hoc'], row['id'])
        return None

    def delete_by_id(self, sv_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM sinh_vien WHERE id = %s"
        cursor.execute(sql, (sv_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True