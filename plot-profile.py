#Définir la police à utiliser
plt.rcParams['font.family'] = 'Arial'

# Création du graphique
ax = plt.subplot(111)

# Tracé du profil de dose relative
ax.plot(axis, (dose / dose[52]) * 100,'-',color='black')  # Normalisation de la dose à la valeur centrale

# Ajouter des lignes verticales pour indiquer les bords du champ 
plt.axvline(x=7, color='red', linestyle='--')
plt.axvline(x=-7, color='red', linestyle='--')


# Ajouter les titres des axes et définir la taille de la police
plt.xlabel('X [mm]', fontsize=20)  # Label pour l'axe X
plt.ylabel('Dose relative [%]', fontsize=20)  # Label pour l'axe Y

# Désactiver la grille pour un affichage plus clair
plt.grid(False)

# Titre du graphique
plt.title('Profil de dose', fontsize=24)

# Masquer les bords droit et supérieur pour un affichage plus propre
ax.spines[['right', 'top']].set_visible(False)

# Affichage du graphique
plt.show()
