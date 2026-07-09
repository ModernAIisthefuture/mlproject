from joblib import load
from django.shortcuts import render
from .forms import BostonForm

# Load trained model
model = load("model.joblib")

def predict(request):
    prediction = None

    if request.method == "POST":
        form = BostonForm(request.POST)

        if form.is_valid():
            data = list(form.cleaned_data.values())
            prediction = model.predict([data])[0]

    else:
        form = BostonForm()

    return render(
        request,
        "predictor/form.html",
        {
            "form": form,
            "prediction": prediction,
        },
    )
