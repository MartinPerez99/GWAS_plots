import subprocess
import pandas as pd
pheno_reference = 'all_pheno.txt'

dataset1 = pd.read_csv(pheno_reference, sep='\t')
columns_to_drop= [col for col in dataset1.columns if not col.startswith('F')]
dataset1.drop(columns=columns_to_drop,inplace=True)

archivos_gwas = []
for i in dataset1.columns:
    pheno_name = i
    index = 0
    for PCA in range(2):
        if index == 0:
            covar = "Covar_def.txt"
            out = f'GWAS_{i}'
            index+=1
        else:
            covar = "CovarPCA_mod1.txt"
            out = f'GWAS_{i}_PCA'


    # Definir el comando que quieres ejecutar
        comando = [
            "plink2",
            "--bfile", "REQUITE_LUNG",
            "--maf", "0.05",
            "--glm", "hide-covar", "cols=+a1freq",
            "--allow-no-sex",
            "--pheno", "all_pheno_mod.txt",
            "--pheno-name", pheno_name,
            "--covar", covar,
            "--covar-variance-standardize",
            "--out", out
        ]

        # Ejecutar el comando en línea de comando
        subprocess.run(comando)
        if i < 5 or i == 5:
            archivo_gwas = out + f'.{i}.glm.linear'
        else:
            archivo_gwas = out + f'.{i}.glm.logistic.hybrid'
        archivos_gwas.append(archivo_gwas)


comando_r = [r'C:\Program Files\R\R-4.2.2\bin\x64\Rscript.exe', r'C:\Users\marti\Desktop\IDIS\Intermediario.R'] + archivos_gwas
subprocess.run(comando_r)