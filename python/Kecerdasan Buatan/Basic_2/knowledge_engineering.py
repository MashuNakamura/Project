def diagnosis(symptom):
    print(f"Gejala yang dimasukkan: {symptom}")
    if symptom == "demam":
        print("Diagnosis: Flu")
        return "Flu"
    elif symptom == "batuk":
        print("Diagnosis: Pilek")
        return "Pilek"
    else:
        print("Diagnosis: Tidak diketahui")
        return "Tidak diketahui"

diagnosis("demam")
diagnosis("batuk")
diagnosis("mual")