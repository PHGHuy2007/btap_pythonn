from database import DatabaseConnection
from models import SinhVien
from repositories import SinhVienRepository

if __name__ == "__main__":
    db = DatabaseConnection("localhost", "root", "", "truong_hoc")
    repo = SinhVienRepository(db)

    sv1 = SinhVien("T2512E", "Phan Hoang GIa Huy", "Công nghệ thông tin")
    repo.save(sv1)

    tat_ca_sv = repo.find_all()
    for sv in tat_ca_sv:
        print(sv)