#!/bin/bash
#SBATCH --job-name=Leakage-1-4mm   # Nom de la tâche
#SBATCH --cpus-per-task=24         # Nombre de CPU par tâche
#SBATCH --time=15:00:00            # Temps d'exécution maximum (hh:mm:ss)
#SBATCH --mem=5G                   # Mémoire allouée par nœud
#SBATCH --mail-type=ALL            # Conditions d'envoi de courriels
#SBATCH --mail-user=patrick-johan.ngontie-ngounou.1@ulaval.ca  # Adresse de courriel pour les notifications
#SBATCH --array=0-359              # Array de tâches pour les 360 angles

# Chemin vers le fichier de données spécifique à chaque tâche de l'array
DATA="./batch/leakage11/leakage${SLURM_ARRAY_TASK_ID}.mac"

# Navigation au dossier contenant l'exécutable de la simulation
cd build

# Chargement du module nécessaire pour exécuter Geant4
module load geant4/11.1.0

# Exécution de la simulation avec le fichier de données correspondant
./prth "-r" 1.6 "-c" $DATA
