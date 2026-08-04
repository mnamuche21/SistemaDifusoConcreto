import numpy as np
import skfuzzy as fuzz
from logica.variables import *

def evaluar(
    Cemento,
    Agua,
    Superplastificante,
    AgregadoFino,
    Edad
):
    # Evaluaciones
    cem_nivel_poco = fuzz.interp_membership(x_cem, cem_poco, Cemento)
    cem_nivel_regular = fuzz.interp_membership(x_cem, cem_regular, Cemento)
    cem_nivel_mucho = fuzz.interp_membership(x_cem, cem_mucho, Cemento)

    agua_nivel_poca = fuzz.interp_membership(x_agua, agua_poca, Agua)
    agua_nivel_regular = fuzz.interp_membership(x_agua, agua_regular, Agua)
    agua_nivel_mucha = fuzz.interp_membership(x_agua, agua_mucha, Agua)

    super_nivel_poco = fuzz.interp_membership(x_super, super_poco, Superplastificante)
    super_nivel_regular = fuzz.interp_membership(x_super, super_regular, Superplastificante)
    super_nivel_mucho = fuzz.interp_membership(x_super, super_mucho, Superplastificante)

    agfi_nivel_poco = fuzz.interp_membership(x_agfi, agfi_poco, AgregadoFino)
    agfi_nivel_regular = fuzz.interp_membership(x_agfi, agfi_regular, AgregadoFino)
    agfi_nivel_mucho = fuzz.interp_membership(x_agfi, agfi_mucho, AgregadoFino)

    edad_nivel_temprana = fuzz.interp_membership(x_edad, edad_temprana, Edad)
    edad_nivel_estandar = fuzz.interp_membership(x_edad, edad_estandar, Edad)
    edad_nivel_madura = fuzz.interp_membership(x_edad, edad_madura, Edad)

    # -----------------------------------------------------------------------------
    # 3. APLICACIÓN DE LAS 19 REGLAS DIFUSAS
    # -----------------------------------------------------------------------------

    # Regla 1: SI Cem=Poco Y Agua=Poca Y Edad=Temprana ENTONCES Res=Regular
    rule1 = np.fmin(np.fmin(cem_nivel_poco, agua_nivel_poca), edad_nivel_temprana)
    act_R1 = np.fmin(rule1, res_regular)

    # Regla 2: SI Cem=Poco Y Agua=Regular Y Super=Poco Y Edad=Temprana ENTONCES Res=Baja
    rule2 = np.fmin(np.fmin(np.fmin(cem_nivel_poco, agua_nivel_regular), super_nivel_poco), edad_nivel_temprana)
    act_R2 = np.fmin(rule2, res_baja)

    # Regla 3: SI Cem=Poco Y Agua=Regular Y Super=Regular Y Edad=Temprana ENTONCES Res=Regular
    rule3 = np.fmin(np.fmin(np.fmin(cem_nivel_poco, agua_nivel_regular), super_nivel_regular), edad_nivel_temprana)
    act_R3 = np.fmin(rule3, res_regular)

    # Regla 4: SI Cem=Poco Y Agua=Regular Y Super=Mucho Y Edad=Temprana ENTONCES Res=Regular
    rule4 = np.fmin(np.fmin(np.fmin(cem_nivel_poco, agua_nivel_regular), super_nivel_mucho), edad_nivel_temprana)
    act_R4 = np.fmin(rule4, res_regular)

    # Regla 5: SI Cem=Poco Y Agua=Mucha Y Edad=Temprana ENTONCES Res=Regular
    rule5 = np.fmin(np.fmin(cem_nivel_poco, agua_nivel_mucha), edad_nivel_temprana)
    act_R5 = np.fmin(rule5, res_regular)

    # Regla 6: SI Cem=Poco Y Edad=Estándar ENTONCES Res=Regular
    rule6 = np.fmin(cem_nivel_poco, edad_nivel_estandar)
    act_R6 = np.fmin(rule6, res_regular)

    # Regla 7: SI Cem=Poco Y Edad=Madura ENTONCES Res=Regular
    rule7 = np.fmin(cem_nivel_poco, edad_nivel_madura)
    act_R7 = np.fmin(rule7, res_regular)

    # Regla 8: SI Cem=Regular Y Super=Poco Y AgFino=Poco ENTONCES Res=Regular
    rule8 = np.fmin(np.fmin(cem_nivel_regular, super_nivel_poco), agfi_nivel_poco)
    act_R8 = np.fmin(rule8, res_regular)

    # Regla 9: SI Cem=Regular Y Super=Poco Y AgFino=Regular ENTONCES Res=Regular
    rule9 = np.fmin(np.fmin(cem_nivel_regular, super_nivel_poco), agfi_nivel_regular)
    act_R9 = np.fmin(rule9, res_regular)

    # Regla 10: SI Cem=Regular Y Super=Poco Y AgFino=Mucho Y Edad=Temprana ENTONCES Res=Baja
    rule10 = np.fmin(np.fmin(np.fmin(cem_nivel_regular, super_nivel_poco), agfi_nivel_mucho), edad_nivel_temprana)
    act_R10 = np.fmin(rule10, res_baja)

    # Regla 11: SI Cem=Regular Y Super=Poco Y AgFino=Mucho Y Edad=Estándar ENTONCES Res=Regular
    rule11 = np.fmin(np.fmin(np.fmin(cem_nivel_regular, super_nivel_poco), agfi_nivel_mucho), edad_nivel_estandar)
    act_R11 = np.fmin(rule11, res_regular)

    # Regla 12: SI Cem=Regular Y Super=Poco Y AgFino=Mucho Y Edad=Madura ENTONCES Res=Regular
    rule12 = np.fmin(np.fmin(np.fmin(cem_nivel_regular, super_nivel_poco), agfi_nivel_mucho), edad_nivel_madura)
    act_R12 = np.fmin(rule12, res_regular)

    # Regla 13: SI Cem=Regular Y Super=Regular ENTONCES Res=Regular
    rule13 = np.fmin(cem_nivel_regular, super_nivel_regular)
    act_R13 = np.fmin(rule13, res_regular)

    # Regla 14: SI Cem=Regular Y Super=Mucho ENTONCES Res=Regular
    rule14 = np.fmin(cem_nivel_regular, super_nivel_mucho)
    act_R14 = np.fmin(rule14, res_regular)

    # Regla 15: SI Cem=Mucho Y Super=Poco ENTONCES Res=Regular
    rule15 = np.fmin(cem_nivel_mucho, super_nivel_poco)
    act_R15 = np.fmin(rule15, res_regular)

    # Regla 16: SI Cem=Mucho Y Super=Regular Y Edad=Temprana ENTONCES Res=Regular
    rule16 = np.fmin(np.fmin(cem_nivel_mucho, super_nivel_regular), edad_nivel_temprana)
    act_R16 = np.fmin(rule16, res_regular)

    # Regla 17: SI Cem=Mucho Y Super=Regular Y Edad=Estándar ENTONCES Res=Alta
    rule17 = np.fmin(np.fmin(cem_nivel_mucho, super_nivel_regular), edad_nivel_estandar)
    act_R17 = np.fmin(rule17, res_alta)

    # Regla 18: SI Cem=Mucho Y Super=Mucho Y Edad=Temprana ENTONCES Res=Regular
    rule18 = np.fmin(np.fmin(cem_nivel_mucho, super_nivel_mucho), edad_nivel_temprana)
    act_R18 = np.fmin(rule18, res_regular)

    # Regla 19: SI Cem=Mucho Y Super=Mucho Y Edad=Estándar ENTONCES Res=Alta
    rule19 = np.fmin(np.fmin(cem_nivel_mucho, super_nivel_mucho), edad_nivel_estandar)
    act_R19 = np.fmin(rule19, res_alta)

    # -----------------------------------------------------------------------------
    # 4. AGREGACIÓN DE REGLAS SEGÚN SU CONSECUENTE
    # -----------------------------------------------------------------------------
    res_act_baja = np.fmax.reduce([act_R2, act_R10])
    res_act_regular = np.fmax.reduce([
        act_R1, act_R3, act_R4, act_R5, act_R6, act_R7,
        act_R8, act_R9, act_R11, act_R12, act_R13, act_R14,
        act_R15, act_R16, act_R18
    ])
    res_act_alta = np.fmax.reduce([act_R17, act_R19])

    # Crear el vector de ceros para el rellenado en la gráfica
    res0 = np.zeros_like(x_res)

    # Agregue las tres funciones de pertenencia de salida juntas
    # con la funcion máximo
    aggregated = np.fmax(res_act_baja,
                        np.fmax(res_act_regular, res_act_alta))

    # Obtener el valor de la resistencia con el metodo del centroide
    resistencia = fuzz.defuzz(x_res, aggregated, 'centroid')

    return resistencia