import skfuzzy as fuzz
import numpy as np

# Crear el dominio de las variables que participan en el sistema
x_cem = np.arange(102, 540, .01) # Cemento : [102,540]
x_agua = np.arange(121.75, 247, .01) # Agua: [121,247]
x_super = np.arange(0, 32.2, .01) # Superplastificante [0,32.2]
x_aggr = np.arange(801, 1145, .01) # Agregado grueso [801,1145]
x_agfi = np.arange(594, 992.6, .01) # Agregado fino [594,992.6]
x_edad =np.arange(1, 365, .01) # Edad [1,365]
x_res = np.arange(2.332, 82.599, 0.01)
# Generar funciones de pertenencia difusas

# Funciones de pertenencia para Cemento
cem_poco = fuzz.trapmf(x_cem, [102, 102, 181.878, 301.461]) # Cemento Poco
cem_regular = fuzz.trimf(x_cem, [181.878, 301.461, 436.298]) # Cemento Regular
cem_mucho = fuzz.trapmf(x_cem, [301.461, 436.298, 540, 540]) # Cemento Mucho

# Funciones de pertenencia para Agua
agua_poca = fuzz.trapmf(x_agua, [121.75, 121.75, 158.074, 189.251]) # Agua Poca
agua_regular = fuzz.trimf(x_agua, [158.074, 189.251, 224.056]) # Agua Regular
agua_mucha = fuzz.trapmf(x_agua, [189.251, 224.056, 247,247]) # Agua Mucha

# Funciones de pertenencia para Superplastificante
super_poco = fuzz.trapmf(x_super, [0, 0, 0.499, 9.241]) # SuperBaja
super_regular = fuzz.trimf(x_super, [0.499, 9.241, 20.012]) # SuperNormal
super_mucho = fuzz.trapmf(x_super, [9.241, 20.012, 32.2, 32.2]) # SuperAlta

# Funciones de pertenencia para AgregadoGrueso
aggr_poco = fuzz.trapmf(x_aggr, [801, 801, 858.348, 963.266]) # AggrPoco
aggr_regular = fuzz.trimf(x_aggr, [858.348, 963.266, 1068.099]) # AggrRegular
aggr_mucho = fuzz.trapmf(x_aggr, [963.266, 1068.099, 1145, 1145]) # AggrMucho

# Funciones de pertenencia para AgregadoFino
agfi_poco = fuzz.trapmf(x_agfi, [594, 594, 661.106, 777.214]) # AgfiPoco
agfi_regular = fuzz.trimf(x_agfi, [661.106, 777.214, 875.597]) # AgfiRegular
agfi_mucho = fuzz.trapmf(x_agfi, [777.214, 875.597, 992.6, 992.6]) # AgfiMucho

# Funciones de pertenencia para Edad
edad_temprana = fuzz.trapmf(x_edad, [1, 1, 22.798, 108.93]) # Edadtemprana
edad_estandar = fuzz.trimf(x_edad, [22.798, 108.93, 326.667]) # Edadestandar
edad_madura = fuzz.trapmf(x_edad, [108.93, 326.667, 365, 365]) # Edadmadura

#Funciones de pertenencia para Resistencia
res_baja = fuzz.trapmf(x_res, [2.332, 2.332, 2.332, 42.466])
res_regular = fuzz.trimf(x_res, [2.332, 42.466, 82.599])
res_alta = fuzz.trapmf(x_res, [42.466, 82.599, 82.599, 82.599])