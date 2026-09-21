from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput
from main.models import Experience, Projects

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "position",
            "organization",
            "description",
            "category",
            "started_at",
            "ended_at",
        ]

        labels = {
            "position": "Posisi Pengalaman",
            "organization": "Organisasi Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "started_at": "Waktu Dimulainya Pengalaman",
            "ended_at": "Waktu Berakhirnya Pengalaman",
        }

        widgets = {
            "position": TextInput(
                attrs={
                    "placeholder": "Asisten Dosen"
            }),
            "organization": TextInput(
                attrs={
                    "placeholder": "Fasilkom UI"
            }),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
            }),
            "category": Select(),
            "started_at": DateTimeInput(
                attrs={
                    "type": "datetime-local"
            }),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local"
            }),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = [
            "title",
            "description",
            "web_link",
            "image_link",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "web_link": "URL Proyek",
            "image_link": "Path Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "web_link": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "image_link": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }