record = "Lovelace,Ada,1815,mathematician"

parts = record.split(",") # "Lovelance" "Ada" "1815" "mathematician"

surname = parts[0] #Lovelance
forename = parts[1] #Ada
born = parts[2] # 1815
role = parts[3] # mathematician

print(f"{forename} {surname} was born in {born} and worked as a {role}.") # Ada Lovelance was born in 1815 and worked as a mathmatician
print(f"Initials: {forename[0]}.{surname[0]}.") # Initials: 
