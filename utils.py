from model import User, BacSi, NguoiBenh, DSKham, PhieuKham, Thuoc, HoaDon
from flask_login import current_user
import hashlib
from __init__ import db 

from sqlalchemy import func
from sqlalchemy.sql import extract



def check_login(username, password):
    
    password = password
    return User.query.filter(User.username.__eq__(username),
                            User.password.__eq__(password)).first()
   

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()
def get_dsNB(ngayDKKham):
    dsNB = DSKham.query
    if ngayDKKham:
        dsNB = dsNB.filter(DSKham.ngayDKKham.contains(ngayDKKham))
    return dsNB.all()

def get_dateDS(ngayDKKham):
    date = DSKham.query
    if ngayDKKham:
        date = date.filter(DSKham.ngayDKKham.__eq__(ngayDKKham)).first()
    return date

def get_dsThuoc(name):
    dsThuoc = Thuoc.query
    if name:
        dsThuoc = dsThuoc.filter(Thuoc.name.contains(name))
    return dsThuoc.all()

def get_lsNB(name):
    dslsNB = PhieuKham.query
    if name:
        dslsNB = dslsNB.filter(PhieuKham.name.contains(name))
    return dslsNB.all()

def get_hdPK(name):
    hoadon = PhieuKham.query
    if name:
        hoadon = hoadon.filter(PhieuKham.name.__eq__(name)).first()
    return hoadon

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_phieukham_by_id(name):
    infor = PhieuKham.query
    if name:
        infor = infor.filter(PhieuKham.name.contains(name))
    return infor.all()

def get_list_userDk():
    return NguoiBenh.query.all()


def register(name, username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, username=username.strip(), password=password)
    db.session.add(u)
    db.session.commit()

def registerDKKham(name, gioitinh, namsinh, phone, ngayDKKham, address, ):
    u = NguoiBenh(name=name, gioiTinh=gioitinh, namSinh=namsinh, phone=phone, ngayDKKham=ngayDKKham, address=address)
    db.session.add(u)
    db.session.commit()

def upDSKham(name, gioitinh, namsinh, ngayDKKham, address):
    u = DSKham(name=name, gioiTinh=gioitinh, namSinh=namsinh, ngayDKKham=ngayDKKham, address=address)
    db.session.add(u)
    db.session.commit()


def updatePK(name, trieuChung, duDoan, ngayKham, ngay, thang):
    u = PhieuKham(name=name, trieuChung=trieuChung, duDoan=duDoan, ngayKham=ngayKham, ngay=ngay, thang=thang, user=current_user)
    db.session.add(u)
    db.session.commit()

def uppdateHD(name, ngayKham, tienKham, tienThuoc, ngayThanhToan, tongTien, id_phieukham):
    u = HoaDon(name=name, tienKham=tienKham, tienThuoc=tienThuoc, ngayKham=ngayKham, user=current_user, ngayThanhToan=ngayThanhToan, tongTien = tongTien, id_PhieuKham=id_phieukham)
    db.session.add(u)
    db.session.commit()


def doanhthu_stats(month):
    p = db.session.query(PhieuKham.ngay, PhieuKham.id, func.sum(HoaDon.tongTien))\
        .join(HoaDon, HoaDon.id_PhieuKham.__eq__(PhieuKham.id))\
        .filter(PhieuKham.thang.contains(month))\
        .group_by(PhieuKham.ngay, PhieuKham.id)
    return p.all()
    

