from django import forms
from .models import Player, Team


class ClanForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("name", "tag", 'agenda')


class PlayerForm(forms.ModelForm):
    """"""
    # Metaを作成することでモデルと紐づける
    class Meta:
        model = Player
        fields = ("registered_date", "psn_id", )


class PlayerUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""
    class Meta:
        model = Player
        fields = ("registered_date", "psn_id", "belong_clan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
