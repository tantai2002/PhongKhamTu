from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from __init__ import db, app
from flask_login import UserMixin, login_manager
from enum import Enum as UserEnum
from datetime import datetime


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key = True, autoincrement = True)

def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    office = Column(String(20), default=True)
    phieukham = relationship('PhieuKham', backref='user', lazy = True)
    hoadon = relationship('HoaDon', backref='user', lazy = True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name

class YTa(BaseModel):
    __tablename__ = 'yta'
    
    name = Column(String(70), nullable = True)
    email = Column(String(100), nullable = True)
    phone = Column(String(10), nullable = True)
    
    def __str__(self):
        return self.name

class BacSi(BaseModel):
    __tablename__ = 'bacsi'
    
    name = Column(String(70), nullable = True)
    email = Column(String(100), nullable = True)
    phone = Column(String(10), nullable = True)
    def __str__(self):
        return self.name

class ThuNgan(BaseModel):
    __tablename__ = 'thungan'
    
    name = Column(String(70), nullable = True)
    email = Column(String(100), nullable = True)
    phone = Column(String(10), nullable = True)
    
    def __str__(self):
        return self.name

class QuanTri(BaseModel):
    __tablename__ = 'quantri'
    
    name = Column(String(70), nullable = True)
    email = Column(String(100), nullable = True)
    phone = Column(String(10), nullable = True)
    
    def __str__(self):
        return self.name

class NguoiBenh(BaseModel):
    __tablename__ = 'nguoibenh'
    name = Column(String(70), nullable = True)
    gioiTinh = Column(String(4), nullable = True)
    namSinh = Column(String(10), nullable = True)
    phone = Column(String(10), nullable = True)
    ngayDKKham = Column(String(10), nullable = True)
    address = Column(String(150), nullable = True)
    id_DSKham = Column(Integer, ForeignKey('dskham.id'))
    def __str__(self):
        return self.name


class Thuoc(BaseModel):
    __tablename__ = 'thuoc'
    name = Column(String(70), nullable = True)
    donViThuoc = Column(String(10), nullable = True)
    soLuongTon = Column(String(3), nullable = True)
    nSX = Column(String(10), nullable = True)
    hSD = Column(String(10), nullable = True)
    
    def __str__(self):
        return self.name

# prod_thuoc = db.Table('prod_thuoc',
#                     Column('thuoc_id', Integer, ForeignKey('thuoc.id'), primary_key=True),
#                     Column('phieukham_id', Integer, ForeignKey('phieukham.id'), primary_key=True))

class DSKham(BaseModel):
    __tablename__ = 'dskham'
    # nguoiBenh = relationship('NguoiBenh', backref = 'nguoibenh', lazy = True)
    name = Column(String(70), nullable = True)
    ngayDKKham = Column(String(10), nullable = True)
    address = Column(String(150), nullable = True)
    namSinh = Column(String(10), nullable = True)
    gioiTinh = Column(String(4), nullable = True)
    nguoiBenh = relationship('NguoiBenh', backref = 'nguoibenh', lazy = True)
    def __str__(self):
        return self.name

class PhieuKham(BaseModel):
    __tablename__ = 'phieukham'
    name = Column(String(70), nullable = False)
    ngayKham = Column(String(10), nullable = False)
    ngay = Column(String(5), nullable = False)
    thang = Column(String(5), nullable = False)
    trieuChung = Column(String(200), nullable = False)
    duDoan = Column(String(200), nullable = False)
    id_User = Column(Integer, ForeignKey(User.id), nullable=False)
    hoadon = relationship('HoaDon', backref = 'phieukham', lazy=True)
    def __str__(self):
        return self.id

# class LichSuBenhNhan(BaseModel):
#     id_PhieuKham = Column(Integer, ForeignKey('phieukham.id'))
#     soLanTaiKham = Column(String(5))

#     def __str__(self):
#         return self.name

class HoaDon(BaseModel):
    __tablename__ = 'hoadon'
    name = Column(String(70), nullable = False)
    ngayThanhToan = Column(String(10), nullable = False)
    tienKham = Column(Float, nullable = True)
    tienThuoc = Column(Float, nullable = True)
    tongTien = Column(Float, nullable = True)
    ngayKham =  Column(String(10), nullable = False)
    id_User = Column(Integer, ForeignKey(User.id), nullable=False)
    id_PhieuKham = Column(Integer, ForeignKey(PhieuKham.id), nullable=False)
    # phieukham = relationship('PhieuKham', backref='hoadon', lazy=True)
    # doanhthu = relationship('DoanhThuThang', backref='hoadon', lazy=True)
    def __str__(self):
        return self.name

# class DoanhThuThang(BaseModel):
#     thang = Column(String(2), nullable = False)
#     ngay = Column(String(10), nullable = False)
#     soBenhNhan = Column(String(3), nullable = False)
#     doanhThu = Column(String(20), nullable = False)
#     tiLe = Column(String(3), nullable = False)
#     id_HoaDon = Column(Integer,ForeignKey(HoaDon.id), nullable=False)
#     def __str__(self):
#         return self.name

# class ThuocSDThang(BaseModel):
#     id_Thuoc = Column(Integer, ForeignKey('thuoc.id'))
#     soLuongSD = Column(String(10), nullable = True)

#     def __str__(self):
#         return self.name

if __name__ == "__main__":
#     with app.app_context():
#             db.create_all()
        
        # password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
        # u = User(name='ThuNgan', username='ThuNgan', password=password,
        #         user_role=UserRole.USER)
        # db.session.add(u)
        # db.session.commit()
    db.create_all()

    # c1 = Category(name='Trang chủ')
    # c2 = Category(name='Máy Tính Bảng')
    # c3 = Category(name='Đồng Hồ Thông Minh')

    # db.session.add(c1)
    # db.session.add(c2)
    # db.session.add(c3)

    # db.session.commit()

#     product = [{
#     "id": 1,
#     "name": "iPhone 7 Plus",
#     "description": "Apple, 32GB, RAM: 3GB, iOS13",
#     "price": 17000000,
#     "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-vang-1-2.jpg",
#     "category_id": 1
#    }, {
#     "id": 2,
#     "name": "iPad Pro 2020",
#     "description": "Apple, 128GB, RAM: 6GB",
#     "price": 37000000,
#     "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-vang-1-2.jpg",
#     "category_id": 2
#    }, {
#     "id": 3,
#     "name": "Galaxy Note 10 Plus",
#    "description": "Samsung, 64GB, RAML: 6GB",
#     "price": 24000000,
#     "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-vang-1-2.jpg",
#     "category_id": 1
#    }, {
#     "id": 4,
#     "name": "iPad Pro 2019",
#     "description": "Apple, 128GB, RAM: 6GB",
#     "price": 37000000,
#     "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-vang-1-2.jpg",
#     "category_id": 2
#    }, {
#     "id": 5,
#     "name": "Iphone 11",
#     "description": "Apple, 128GB, RAM: 6GB",
#     "price": 37000000,
#     "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-vang-1-2.jpg",
#     "category_id": 2
#    }
#    , {
#     "id": 5,
#     "name": "Iphone 12",
#     "description": "Apple, 128GB, RAM: 6GB",
#     "price": 37000000,
#     "image": "https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-vang-1-2.jpg",
#     "category_id": 2
#    }
# ]

#     for p in product:
#         pro = Product(name=p['name'], price=p['price'], image=p['image'], description=p['description'], category_id=p['category_id'])

#         db.session.add(pro)





#     db.session.commit()
    


