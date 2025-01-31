def sum_and_write(input_files, output_file):
    # Colonnes à sommer
    columns_to_sum = [3, 4, 5]  # Indices des colonnes de dose, dose au carré, et nombre d'entrées

    # Dictionnaire pour stocker les totaux par indice (iX, iY, iZ)
    totals = {}

    for file in input_files:
        with open(file, "r") as file:
            lines = file.readlines()

        for line in lines:
            if not line.startswith("#"):
                values = line.strip().split(",")
                iX, iY, iZ = map(int, values[:3])  # Coordonnées iX, iY, iZ

                # Initialisation des totaux si les coordonnées n'existent pas déjà
                if (iX, iY, iZ) not in totals:
                    totals[(iX, iY, iZ)] = [0.0, 0.0, 0]  # Initialisation pour les valeurs de dose, dose au carré, et entrées

                # Addition des valeurs des colonnes spécifiées
                for col_index in columns_to_sum:
                    col_value = float(values[col_index])
                    totals[(iX, iY, iZ)][col_index - 3] += col_value

    # Écriture des résultats dans le fichier de sortie
    with open(output_file, "w") as file:
        file.write("#iX, iY, iZ, total(value) [Gray], total(val^2), entries\n")
        for (iX, iY, iZ), (total_values, total_squared, total_entries) in totals.items():
            file.write(f"{iX},{iY},{iZ},{total_values},{total_squared},{total_entries}\n")
