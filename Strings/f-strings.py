# It is new sring formatting mechanism introduced by the PEP 498.It is also knownas literal string Interpolation or more commonly as F-strings.

letter = "Kenji is visiting Japan to explore its historic temples."

name = "Harry"
country = "Japan"

print(f"{name} is visiting {country} to explore its historic temples.")
print(f"{{name}} is visiting {{country}} to explore its historic temples.")

price = 34.03333

text = f"For only {price:.2f} dollars!"
print(text)

print(f"{3*31}")
print(type(f"{3*31}"))

