from flask import render_template, request, redirect, session, jsonify, sessions
from __init__ import app, login
import utils
from admin import *
from flask_login import login_user, current_user, login_required, logout_user
from decorators import annonymous_user
import datetime



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/indexNB")
def homeNB():
    return render_template('indexNB.html')

@app.route("/indexNV")
def homeNV():
    return render_template('indexNV.html')

@app.route('/dsNB')
def dsNB():
    return render_template('danhsachNB.html')

@app.route("/backListDK")
def backListDK():
    return render_template('indexNV.html')   

@app.route("/backLapPK")
def backLapPK():
    return render_template('indexNV.html')  

@app.route("/traCuuThuoc")
def traCuuThuoc():
    return render_template("traCuuThuoc.html")

@app.route("/traCuuLSBenh")
def traCuuLSBenh():
    return render_template("traCuuLSBenh.html")

#login admin
@app.route('/admin-login', methods=['post'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    user = utils.check_login(username=username, password=password)
    if user:
        login_user(user=user)
    return redirect('/admin')



#login người bệnh
@app.route('/login', methods=['get', 'post'])
@annonymous_user
def login_my_user():
    if request.method.__eq__('POST'):
        username = request.form['username']
        password = request.form['password']
        user = utils.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            n = request.args.get('next')
            return redirect(n if n else '/indexNB')

    return render_template('login.html')


#login nhân viên
@app.route('/loginNV', methods=['get', 'post'])
# @annonymous_user
def login_my_nv():
    nguoibenh = utils.get_list_userDk()
    if request.method.__eq__('POST'):
        username = request.form['username']
        password = request.form['password']
        user = utils.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            return render_template('/indexNV.html', nguoibenh=nguoibenh)

    return render_template('loginNV.html')


#đăng ký tài khoản
@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):
            
            try:
                utils.register(name=request.form['name'],
                             username=request.form['username'],
                             password=password)
                return redirect('/login')
            except:
                err_msg = 'Hệ thống đang có lỗi! Vui lòng quay lại sau!'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)

#logout Người bệnh
@app.route('/logout')
def logout_my_user():
    logout_user()
    # return redirect('/login')
    return render_template('index.html')


#logout Nhân viên
@app.route('/logoutNV')
def logout_my_NV():
    logout_user()
    return render_template('loginNV.html')


#đăng ký khám
@app.route('/dk-kham', methods=['POST'])
def dk_kham():
    err_msg = ''
    name=request.form['name']
    if request.method.__eq__('POST'):
        try:
            utils.registerDKKham(
                                name=name,
                                gioitinh=request.form['gioitinh'],
                                namsinh=request.form['namsinh'],
                                phone=request.form['phone'],
                                ngayDKKham=request.form['ngayDKKham'],
                                address=request.form['address']
            )
            return redirect('/indexNB')
        except:
                    err_msg = 'Hệ thống đang có lỗi! Vui lòng quay lại sau!'
                

    return render_template('indexNB.html', err_msg=err_msg)
    

#ghi nhận đăng nhập
@login.user_loader
def load_login(user_id):
    return utils.get_user_by_id(user_id)

#lập danh sách nguòi bệnh
@app.route('/ds-kham', methods=['POST'])
def lapDS():
    data = request.json
   
    # import pdb
    # pdb.set_trace()
 
    name = data.get('name')
    gioitinh = data.get('gioiTinh')
    namsinh = data.get('namSinh')
    ngayDKKham = data.get('ngayDKKham')
    address = data.get('address')   
    
    utils.upDSKham(
                    name = name,
                    gioitinh = gioitinh,
                    namsinh = namsinh,
                    ngayDKKham = ngayDKKham,
                    address = address     
    )

    return 

#Xem ds đã lập
@app.route('/searchDSNB', methods = ['post', 'get'])
def searchDSNB():
    
    ngayDKKham = request.form['searchDate']
    filterDK = utils.get_dateDS(ngayDKKham=ngayDKKham)
    dsNB = utils.get_dsNB(ngayDKKham=ngayDKKham)
    return render_template('danhsachNB.html', dsNB=dsNB, filterDK=filterDK)

#Lưu phiếu khám

@app.route('/addPhieuKham', methods=['post'])
def addPhieuKham():
    name=request.form['name']
    a = datetime.datetime.now()
    b = a.strftime("%d/%m/%Y")
    if name:
        utils.updatePK(
            name=name,
            trieuChung=request.form['trieuChung'],
            duDoan=request.form['duDoan'],
            ngayKham=b
            # ngay=a.strftime("%d"),
            # thang=a.strftime("%m"),
        )
        return render_template('indexNV.html')
    return render_template('indexNV.html')

#lưu hóa đơn
@app.route('/addHoaDon', methods=['post'])
def addHoaDon():
    a = datetime.datetime.now()
    b = a.strftime("%d/%m/%Y")
    name=request.form['name']
    get_idPK = utils.get_hdPK(name=name)
    if name:
        utils.uppdateHD(
            name=request.form['name'],
            ngayKham=request.form['ngayKham'],
            tienKham=request.form['tienKham'],
            tienThuoc=request.form['tienThuoc'],
            ngayThanhToan = b,
            ngay=a.strftime("%d"),
            thang=a.strftime("%m"),
            tongTien = request.form['tongTien'],
            id_phieukham = get_idPK.id
        )
        return render_template('indexNV.html')
    return render_template('indexNV.html')

#tra cứu thuốc
@app.route('/searchThuoc', methods = ['post'])
def searchThuoc():
    
    nameThuoc = request.form['searchThuoc']
    dsThuoc = utils.get_dsThuoc(name=nameThuoc)
    return render_template('traCuuThuoc.html', dsThuoc=dsThuoc)

#tra cứu ls bệnh
@app.route('/searchLSNB', methods = ['post'])
def searchLSNB():
    nameNB = request.form['searchLSNB']
    dsLSNB = utils.get_lsNB(name=nameNB)
    return render_template('traCuuLSBenh.html', dsLSNB=dsLSNB)

#tìm phiếu khám
@app.route('/searchPK', methods = ['post'])
def searchPK():
    namePK = request.form['searchPK']
    dshdPK = utils.get_hdPK(name=namePK)
    return render_template('indexNV.html', dshdPK=dshdPK)




if __name__ == '__main__':
    app.run(debug=True)