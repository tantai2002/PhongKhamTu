from model import NguoiBenh, UserRole, Thuoc
from __init__ import app, db, admin
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_login import logout_user, current_user
from flask import redirect, request, render_template
import utils
import datetime
from flask_admin.contrib.sqla import ModelView


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class logoutView(AuthenticatedView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    
class statsView(AuthenticatedView):
    @expose('/')
    def index_thang(self):
        a = str(request.args.get('searchThang'))
        stats = utils.doanhthu_stats(a)
        sl_stats = utils.slBenhNhan_stats(a)
        dem = 0
        tile = 0
        p = 0
        for p  in sl_stats:
            dem+=1
        tile = dem / 40
        return self.render('admin/stats.html', stats=stats, sl=dem, thang = a, tile=tile)
    

admin.add_view(AuthenticatedModelView(NguoiBenh, db.session, 'Người Bệnh'))
admin.add_view(AuthenticatedModelView(Thuoc, db.session, 'Thuốc'))
admin.add_view(logoutView('Đăng xuất'))
# admin.add_view(MyAdminIndex(HoaDon, db.session, 'Thống kê báo cáo'))
admin.add_view(statsView('Thống kê'))
