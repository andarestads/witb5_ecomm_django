from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from . models import ProdukItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProdukItem
        fields =  ['nama_produk', 'harga', 'harga_diskon', 'slug', 'deskripsi', 'gambar', 'label', 'kategori', 'katalog']
        widgets = {
            'nama_produk': forms.FileInput(attrs={'class': 'form-control'}),
            'harga': forms.FileInput(attrs={'class': 'form-control'}),
            'harga_diskon': forms.FileInput(attrs={'class': 'form-control'}),
            'slug': forms.FileInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.FileInput(attrs={'class': 'form-control'}),
            'gambar': forms.FileInput(attrs={'class': 'form-control'}),
            'label': forms.Select(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'katalog': forms.Select(attrs={'class': 'form-control'}),
        }

PILIHAN_PEMBAYARAN = (
    ('P', 'Paypal'),
    ('S', 'Stripe'),
)

class CheckoutForm(forms.Form):
    alamat_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Alamat Anda', 'class': 'textinput form-control'}))
    alamat_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Apartement, Rumah, atau yang lain (opsional)', 'class': 'textinput form-control'}))
    negara = CountryField(blank_label='(Pilih Negara)').formfield(widget=CountrySelectWidget(attrs={'class': 'countryselectwidget form-select'}))
    kode_pos = forms.CharField(widget=forms.TextInput(attrs={'class': 'textinput form-outline', 'placeholder': 'Kode Pos'}))
    simpan_info_alamat = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    opsi_pembayaran = forms.ChoiceField(widget=forms.RadioSelect(), choices=PILIHAN_PEMBAYARAN)