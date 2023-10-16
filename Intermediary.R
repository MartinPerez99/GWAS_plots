library(vroom)
#Proband
args <- commandArgs(trailingOnly = TRUE)
for (i in args) {
  #generar id para pdf
  nombrecompleto <- i
  id <- sub(".*PRUEBAAGWAS_(.*?)\\.F.*", "\\1", i)
  titulo <- paste("Resultados GWAS para ", id,sep = "")
  #lectura datos
  #ruta_archivo <- paste("/hdd/Martin/GWAS-Nuevosdatos/GWAS_genotypes/Datosbuenos/", i, sep = "")
  #archivo<-vroom(ruta_archivo)
  out <- paste("C:/Users/marti/Desktop/IDIS/", id, ".html", sep = "")
  archivo<-vroom(nombrecompleto)
  colnames(archivo)[colnames(archivo) == "#CHROM"] <- "CHR"
  colnames(archivo)[colnames(archivo) == "OBS_CT"] <- "OBS_CT"
  colnames(archivo)[colnames(archivo) == "ID"] <- "SNP"
  colnames(archivo)[colnames(archivo) == "POS"] <- "BP"
  rmarkdown::render("C:/Users/marti/Desktop/IDIS/Manhattan_QQplot.Rmd", params = list(titulo = titulo, archivo = archivo, id = id), output_file = out)
}

