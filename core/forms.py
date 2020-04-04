from django import forms


class SaleForm(forms.Form):
    ean_add = forms.CharField(
        label="Artikel hinzufügen",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            },
        ),
    )

    ean_remove = forms.CharField(
        label="Artikel entfernen",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            },
        ),
    )

    balance = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control text-right",
            },
        ),
    )

    deposit_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            },
        ),
    )


class CashbookForm(forms.Form):
    start = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "TT.MM.JJJJ",
            },
        ),
    )

    end = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "TT.MM.JJJJ",
            },
        ),
    )

    update = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control text-right",
                "placeholder": "Betrag",
            },
        ),
    )
