# Daftar aturan berbentuk (premis, konklusi)
rules = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
]

# Fakta awal dari user (bisa lebih dari satu)
initial_facts = input("Masukkan fakta awal (pisahkan dengan koma, contoh: A,B): ")
facts = set(f.strip().upper() for f in initial_facts.split(",") if f.strip())

print("Fakta awal:", facts)

# Proses forward chaining
while True:
    applied = False
    for premise, conclusion in rules:
        if premise in facts and conclusion not in facts:
            print(f"Karena punya {premise}, dapat {conclusion}")
            facts.add(conclusion)
            applied = True
    if not applied:
        break

print("Semua fakta yang diperoleh:", sorted(facts))