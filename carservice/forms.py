from django import forms
from django.forms import ModelForm
from carservice.models import *
from django.utils.translation import ugettext_lazy as _
from phonenumber_field import widgets
from ckeditor.widgets import CKEditorWidget

MANU_CHOOSE = (('AUDI','AUDI'), ('BMW','BMW'), ('CHEVROLET','CHEVROLET'),('FORD','FORD'),('TOYOTA','TOYOTA'),( 'HONDA', 'HONDA'),('HYUNDAI','HYUNDAI') , ('ISUZU','ISUZU'),('KIA','KIA') , ('LAND ROVER','LAND ROVER'),('LEXUS','LEXUS') ,('MAZDA','MAZDA') , ('MERCEDES-BENZ','MERCEDES-BENZ'),('MITSUBISHI','MITSUBISHI') ,('NISSAN','NISSAN') , ('PEUGEOT','PEUGEOT'),('PORSCHE','PORSCHE') ,('RENAULT','RENAULT') , ('SUZUKI','SUZUKI'), ('VOLKSWAGEN','VOLKSWAGEN'), ('FUSO','FUSO'), ('HINO','HINO'), ('INFINITI','INFINITI'), ('JAGUAR','JAGUAR'), ('LAMBORGINI','LAMBORGINI'), ('LUXGEN','LUXGEN'), ('MASERATI','MASERATI'), ('MINI','MINI'), ('ROLLS ROYCE','ROLLS ROYCE'), ('SAMSUNG','SAMSUNG'), ('SUBARU','SUBARU'), ('SYM','SYM'), ('THACO','THACO'), ('VINAXUKI','VINAXUKI'), ('VOLVO','VOLVO'))
permision_choose = ((1, 'Chỉ được thêm mới dữ liệu'), (2, 'Được thêm, xóa, sửa dữ liệu'))
class CarForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Car
		fields = ['carid', 'nameofcar', 'locate_code', 'manufacturer','owner', 'typecar', 'yearofmanu', 'avatar']
		labels = {
			'carid' : _('Tên xe'),
			'nameofcar' : _("Tên xe. ví dụ: Fotuner"),
			'manufacturer' : _("Hãng xe. ví dụ: Toyota"),
			'owner' : _("Chủ sở hữu. ví dụ: Nguyễn văn tèo"),
			'typecar' : _("Loại xe. ví dụ: 16 Chỗ"),
			'yearofmanu' : _("Đời xe. ví dụ: 2015"),
			'avatar' : _("Ảnh đại diện"),
			'locate_code' : _("Mã định vị"),
		}
		widgets = {
			'carid': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nhập biển số xe', 'name': 'carid'}),
			'nameofcar': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên xe, ví dụ: Fortuner', 'name': 'nameofcar'}),
			'manufacturer' : forms.Select(choices = MANU_CHOOSE, attrs={'class': 'form-control', 'name': 'manufacturer'}), #forms.Select(attrs={'class': 'form-control', 'name': 'manufacturer'Ư)
			'owner': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Chủ xe, vd: Nguyễn Văn Tèo', 'name': 'owner'}),
			'typecar': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Loại xe, vd 16 chỗ', 'name': 'typecar'}),
            'yearofmanu': forms.TextInput(attrs={'class': 'form-control', 'name': 'yearofmanu'} ), #
            'avatar' : forms.FileInput(attrs={'class': 'form-control', 'name': 'avatar'}), #
            'locate_code' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Mã hộp đen', 'name': 'locate_code'}),

        }

# class ManuForm(object):
# 	"""docstring for ManuForm"""
# 	class Meta:
# 		model = ManuFacturers
# 		fields = ơ'name'ư
# 		label = Ơ
# 			'name' : 'Tên hãng'
# 		Ư
# 		widgets{
# 			'name' : forms.TextInput(attrs=Ơ'class': 'form-control','placeholder': 'Hãng Sản xuất xe', 'name': 'name'Ư),
# 		Ư
			
		
class DriverForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Driver
		fields = ['idcard', 'drivername', 'phone_number', 'address', 'birthday', 'experience','introduce', 'avatar']
		widgets = {
			'idcard': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nhập chứng minh nhân dân', 'name': 'idcard'}),
			'drivername': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên tài xế', 'name': 'drivername'}),
			'phone_number': widgets.PhoneNumberPrefixWidget(attrs={'class': 'form-control','placeholder': 'Nhập số điện thoại', 'name': 'phone_number'}),
			'address' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Địa chỉ thường trú', 'name': 'address'}),
			'birthday': forms.DateInput(attrs={'id':'datepicker', 'class': 'form-control', 'name': 'age'}), #attrs={'class': 'form-control', 'name': 'age'}
            'experience' : forms.NumberInput(attrs={'class': 'form-control', 'name': 'experience'}), #attrs={'class': 'form-control', 'name': 'experience'}
			'introduce': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Giới  thiệu đôi chút về bản thân',  'name': 'introduce'}),
			'avatar' : forms.FileInput(attrs={'class': 'form-control', 'name': 'avatar'}), #
        }

class AlbumForm(ModelForm):  
	"""docstring for Contacts"""
	class Meta:
		model = Album
		fields = ['title', 'decription']
		labels = {
			'title' : 'Tên Album',
			'decription' : 'Mô tả'
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'title'}),
			'decription': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Thêm mô tả',  'name': 'decription'}),
        }
class PhotoForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Photo
		fields = ['path_img', 'comment_img']
		labels = {
			'path_img' : 'Đường dẫn',
			'comment_img' : 'Mô tả'
		}
		widgets = {
			# 'album': forms.TextInput(attrs={'readonly':'True','class': 'form-control','placeholder': 'Tên album', 'name': 'album'}),#ModelChoiceField(queryset= Album.objects.all()),
			'path_img': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Tên album', 'name': 'path_img'}),			
			'comment_img': forms.Textarea(attrs={'cols': 30, 'rows': 5, 'class': 'form-control','placeholder': 'Thêm mô tả',  'name': 'comment_img'}),
		}

class ScheduleForm(ModelForm):
	"""docstring for Contacts"""
	# car = forms.ModelMultipleChoiceField(queryset=Car.objects.all())
	class Meta:
		model = Schedule
		fields = ['departure_day', 'destination_day', 'departure', 'destination', 'departure_time', 'price', 'deposit', 'status']
		labels = {
			# 'car' : 'Loại Xe (Biển số)',
			'departure_day' : "Ngày khởi hành",
			'destination_day' : "Ngày về",
			'departure' : "Địa điểm khởi hành",
			'destination' : "Điểm đến",
			'departure_time' : "Thời gian xuất phát",
			'price' : "Giá",
			'deposit' : "Tiền cọc",
			'status' : "Trạng thái",
		}
		widgets = {
			# 'car': forms.Select(attrs={'class': 'form-control', 'name': 'car'}), #, attrs={'class': 'form-control','placeholder': 'Xe', 'name': 'car'}
			'departure_day': forms.DateInput(attrs={'id':'datepicker1','class': 'form-control','placeholder': 'Ngày khởi hành', 'name': 'departure_day'}),
			'destination_day': forms.DateInput(attrs={'id':'datepicker2','class': 'form-control','placeholder': 'Ngày về', 'name': 'destination_day'}),
            'departure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nơi khởi hành','name': 'departure'} ), #
            'destination' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Điểm đến cuối cùng', 'name': 'destination'}), #
            'departure_time': forms.TimeInput(attrs={'id':'timepicker1', 'class': 'form-control','placeholder': 'Giờ khởi hành', 'name': 'departure_time'}),
			'price': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiền cho mướn xe', 'name': 'price'}),
            'deposit': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiền cọc', 'name': 'deposit'} ), #
            'status': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Trạng thái', 'name': 'status'} ), #
        }

class CostForm(ModelForm):
	"""docstring for Contacts"""
	class Meta:
		model = Cost
		fields = ['schedule', 'total_revenue', 'spent_oil', 'spent_steersman', 'spent_arises']
		labels = {
			'schedule' : 'Lịch trình',
			'total_revenue' : "Gía cho mướn xe",
			'spent_oil' : "Phí xăng dầu",
			'spent_steersman' : "Phí tài xế",
			'spent_arises' : "Các loại phí khác",
			
		}
		widgets = {
			'schedule': forms.Select(attrs={'class': 'form-control', 'name': 'schedule'}),
			'total_revenue': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiền cho thuê xe', 'name': 'total_revenue'}),
			'spent_oil': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Chi phí nhiên liệu (Tiền xăng dầu)', 'name': 'spent_oil'}),
			'spent_steersman' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Phí tài xế', 'name': 'spent_steersman'}),
			'spent_arises' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Phí phát sinh (tiền phạt, phí đường bộ...)', 'name': 'spent_arises'}),
			
        }

class UserLoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		label = {
			'username': 'Tên đăng nhập',
			'password': 'Mật khẩu',
		}
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tài khoản đăng nhập', 'name': 'username'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Nhập mật khẩu', 'name': 'password'}),
			
        }
class UserRegisterForm(ModelForm):
	confirm_password=forms.CharField(label=_("Nhập lại mật khẩu"), widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Nhập lại mật khẩu', 'name': 'confirm_password'}))
	class Meta:
		model = User
		fields = ['fullname','username', 'password', 'confirm_password', 'phone', 'permision']
		labels = {
			'username': 'Tên đăng nhập',
			'fullname': 'Họ tên',
			'password': 'Mật khẩu',
			# 'confirm_password': 'Nhập lại mật khẩu',
			'phone': 'Số điện thoại',
			'permision': 'Phân quyên'
		}
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tài khoản đăng nhập', 'name': 'username'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Nhập mật khẩu', 'name': 'password'}),
			# 'confirm_password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Nhập lại mật khẩu', 'name': 'confirm_password'}),
			'fullname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Họ tên', 'name': 'fullname'}),
			'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số điện thoại', 'name': 'phone'}),
			'permision': forms.Select(choices = permision_choose, attrs={'class': 'form-control', 'name': 'permision'}),
			
        }
  #   def clean(self):
		# cleaned_dât = super(UseregisterForm, self).clean()
  #       pasword = cleaned_data.get("pasword")
  #       confirm_pasword = cleaned_data.get("confirm_pasword")
  #       if pasword != confirm_pasword:
  #           raise forms.ValidationError("Mật khẩu nhập lại khồng khớp")
  #          
class ContentForm(ModelForm):
	class Meta:
		model = Content
		fields = ['avatar', 'title', 'phone', 'address', 'email', 'link', 'summary']
		labels = {
			'avatar' : 'Ảnh đại diện',
			'title' : "Tên dịch vụ",
			'phone' : "Đường dây nóng",
			'address' : "Địa chỉ",
			'email' : "địa chỉ mail",
			'link' : "Các trang mạng liên kết",
			'summary': "Giớ thiệu công ty",
		}
		widgets = {
			'avatar': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Ảnh đại diện công ty', 'name': 'avatar'}),
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên dịch vụ', 'name': 'title'}),
			'phone': widgets.PhoneNumberPrefixWidget(attrs={'class': 'form-control','placeholder': 'Số điện thoại', 'name': 'phone'}),
			'email' : forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Nhâp địa chỉ mail', 'name': 'email'}),
			'address' : forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Phí phát sinh (tiền phạt, phí đường bộ...)', 'name': 'address'}),
			'link': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiền cho thuê xe', 'name': 'link'}),
			'summary': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Nội dung trang web', 'name': 'summary'}),
		}

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'content']
		labels = {
			'title' : "Tiêu đề bài viết",
			'content' : "Nội dung",
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tên dịch vụ', 'name': 'title'}),
			'content': CKEditorWidget(),
		}

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['title', 'content']
		labels = {
			'title' : "Tiêu đề",
			'content' : "Bình luận",
		}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tiêu đề bình luận', 'name': 'title'}),
			'content':  forms.Textarea(attrs={'class': 'form-control','placeholder': 'Nội dung bình luận', 'name': 'summary'}),
		}
		
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ['cName', 'cAvatar', 'cPhone', 'cAddress', 'cID']
		labels = {
			'cName' : "Họ tên",
			'cAvatar' : "Ảnh đại diện",
			'cPhone' : 'Số điện thoại',
			'cAddress' : 'Địa chỉ',
			'cID' : 'Chứng minh thư'
		}
		widgets = {
			'cName': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Họ tên khách hàng', 'name': 'cName'}),
			'cPhone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số điện thoại khách hàng', 'name': 'cPhone'}),
			'cAddress': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Địa chỉ nhà', 'name': 'cAddress'}),
			'cID': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Số chứng minh nhân dân', 'name': 'cID'}),
			'cAvatar': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ảnh đại diện', 'name': 'cAvatar'}),
			
		}