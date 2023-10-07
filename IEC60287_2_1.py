import pandas as pd
import math
with pd.ExcelFile("D:\Carlos_Cloud Folders\OneDrive\JupyterProjects\IEC\IEC60287_2_1.xlsx") as xls:
    _table1 = pd.read_excel(xls, "table1", skiprows=4, dtype='string', header=None, names=[1,2,3])
    _table2 = pd.read_excel(xls, "table2", skiprows=4, dtype='string', header=None, names=[1,2,3,4,5,6])
    _table3 = pd.read_excel(xls, "table3", skiprows=3, dtype='string', header=None, names=[1,2])
    _table4 = pd.read_excel(xls, "table4", skiprows=4, dtype='string', header=None, names=[1,2,3,4])

def table1(material="", material_application="Dont_Care"):
        
    """
    This FUNCTION looks up the thermal resistivity 'Pt' of a material.

    REQUIRED:
        **material** (string, None) - Material code. Refer to dictionary below.

    OPTIONAL:
        **application** (string, "Dont_Care")   - "insulation" for insulation material application, 
                                                - "oversheath" for Protective covering
                                                - "duct" for material used for duct installation
                                                - "Dont_Care" returns value with the highest thermal resisitivity

    OUTPUT:
        **pt_thermal_resistivity** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        thermal_resistivity, error_code = table1("PVC>3kV", "insulation")
    """
    _row_application={
        "insulation":1,     #   Insulating materials                             
        "oversheath":2,     #   Protective covering          
        "duct":3,           #   Materials for duct installation
        "Dont_Care":4,      #   Parses through material options and returns highest thermal resistivity
        }
    _row_insulation={
        "PI-Solid":1,       #   Insulating materials:   Paper insulation in solid type cables                          
        "PI-Oil":2,         #                           Paper insulation in oil-filled cables 
        "Gas":3,            #                           Paper insulated in cables with external gas pressure
        "Gas-PI":4,         #                           Paper insulation in cables with internal gas pressure: pre-impregnated
        "Gas-MI":5,         #                           Paper insulation in cables with internal gas pressure: mass-impregnated
        "PE":6,             #                           PE
        "XLPE":7,           #                           Cross linked Polyelthelyne
        "PVC":8,            #                           PVC up to and including 3kV
        "PVC>3kV":9,        #                           PVC greater than 3kV
        "EPR":10,           #                           EPR up to and including 3kV
        "EPR>3kV":11,       #                           EPR greater than 3kV
        "IIR":12,           #                           Butyl rubber
        "SiR":13,           #                           Rubber
        }
    _row_cover={
        "Jute":14,          #   Protective covering:    Compounded jute and fibrous materials
        "R.Sandwich":15,    #                           Rubber sandwich protection
        "CR":16,            #                           Polychloroprene
        "PVC":17,           #                           PVC up to and including 35kV
        "PVC>3kV":18,       #                           PVC/bitumen on corrugated aluminium sheaths
        "PVC-Bit":19,       #                           PVC/bitumen on corrugated sheaths
        "PE":20,            #                           PE
        }
    _row_duct={
        "Concrete":21,      #   Materials for duct installation:    Concrete
        "Fibre":22,         #                                       Fibre
        "Asbestos":23,      #                                       Asbestos
        "Earthenware":24,   #                                       Earthenware
        "PVC":25,           #                                       PVC
        "PE":26             #                                       PE
        }
    _error_code = []
    try:
        _group = _row_application[material_application]
    except:
        print("Unexpected value or type for parameter 'material_application'")
        raise 
    if _group == 1:
        try:
            _row = _row_insulation[material]
        except:
            print("Unexpected value or type for parameter 'material' for chosen 'material_application'")
            raise
    elif _group == 2:
        try:
            _row = _row_cover[material]
        except:
            print("Unexpected value or type for parameter 'material' for chosen 'material_application'")
            raise
    elif _group == 3:
        try:
            _row = _row_duct[material]
        except:
            print("Unexpected value or type for parameter 'material' for chosen 'material_application'")
            raise
    else:
        _row = []
        count = 0
        try:
            _row.append(_row_insulation[material])
            count = + 1
        except:
            pass
        try:
            _row.append(_row_cover[material])
            count = + 1
        except:
            pass
        try:
            _row.append(_row_duct[material])
            count = + 1
        except:
            pass
        if count == 0:
            _row = _row[0]
        elif count == 0:
            print("Unexpected value or type for parameter 'material' for chosen 'material_application'")              
        else:
            _row = max(_row)
    pt_thermal_reistivity = float(_table1.iloc[_row][3])
    return(pt_thermal_reistivity, _error_code)
    
def table2(installation_method="", clipped_direct="Dont_Care"):

    """
    This FUNCTION looks up the Z_coefficent, E_constant and g_coefficent factors associated with the cable method of installation.

    REQUIRED:
        **installation_method** (string, None) - installation method code. Refer to dictionary below.

    OPTIONAL:
        **clipped_direct** (string, "Dont_Care")    - "yes" for clipped driect method where De<=0.08m, 
                                                    - "no" for cable installation on supports where De<=0.15m
                                                    - "Dont_Care" returns values corresponding with the highest Z

    OUTPUT:
        **Z_coefficent** (float) 
        **E_constant** (float) 
        **g_coefficent** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        Z, E, g, error_code = table1("3CTT", "no")
    """

    _row_group={
        "no":1,    
        "yes":2,  
        "Dont_Care":3
        }
    _row_not_direct={
        "1C":1,    #   Single cable
        "2CTH":2,  #   Two cables touching, horizontal
        "3CTT":4,  #   Three cables in trefoil
        "3CTH":5,  #   Three cables touching, horizontal
        "2CTV":6,  #   Two cables touching vertical
        "2CSV":7,  #   Two cables spaced D, vertical
        "3CTV":8,  #   Three cables touching, vertical
        "3CSV":9   #   Three cables space D, vertical
        }
    _row_clipped_direct={
        "1C":10,   #   Single cable
        "3CTT":11  #   Three cables in trefoil
        }
    _error_code = []
    try:
        _group = _row_group[clipped_direct]
    except:
        print("Unexpected value or type for parameter 'clipped_direct'")
        raise 
    if _group == 1:
        try:
            _row = _row_not_direct[installation_method]
        except:
            print("Unexpected value or type for parameter 'installation_method' or 'clipped_direct'")
            raise
    elif _group == 2:
        try:
            _row = _row_clipped_direct[installation_method]
        except:
            print("Unexpected value or type for parameter 'installation_method' or 'clipped_direct'")
            raise
    else:
        _row = []
        count = 0
        try:
            _row.append(_row_not_direct)
            count = + 1
        except:
            pass
        try:
            _row.append(_row_clipped_direct)
            count = + 1
        except:
            pass
        if count == 1:
            _row = _row[1]
        elif count == 0:
            print("Unexpected value or type for parameter 'installation_method' or 'clipped_direct'")            
        else:
            _row = max(_row)
    Z_coefficent = float(_table2.iloc[_row][3])
    E_constant = float(_table2.iloc[_row][4])
    g_coefficent = float(_table2.iloc[_row][5])
    return(Z_coefficent, E_constant, g_coefficent, _error_code)

def table3(serving_material=""):

    """
    This FUNCTION looks up absorption coefficient of solar radiation for cable surfaces.

    REQUIRED:
        **serving_material** (string, None) 

    OPTIONAL:

    OUTPUT:
        **rho** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        rho, error_code = table3("PVC")
    """

    _row_serving={
        "Jute":1,       # Bitumen/jute serving                          
        "CR":2,         # Polychloroprene 
        "PVC":3,        # PVC
        "PE":4,         # PE
        "Pb":5,         # Lead
        }

    _error_code = []
    try:         ##Function style maintained in order to potentially consolidate into a future standardised function
        _group = 1
    except:
        ##no purpose##
        raise 
    if _group == 1:
        try:
            _row = _row_serving[serving_material]
        except:
            print("Unexpected value or type for parameter 'serving_material'")
            raise
    rho = float(_table3.iloc[_row][2])
    return(rho, _error_code)

def table4(duct_material=""):

    """
    This FUNCTION looks up values for U_constant, V_constant and Y_coefficient.

    REQUIRED:
        **duct_material** (string, None) 

    OPTIONAL:

    OUTPUT:
        **U_constant** (float) 
        **V_constant** (float)
        **Y_coefficient** (float)
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        U, V, lambda, error_code = table4("3CTT", "no")
    """

    _row_material={
        "MC":1,     # In metallic conduit                          
        "FA":2,     # In fibre duct in air 
        "FC":3,     # In fibre duct in concrete
        "AA":4,     # In asbestos cement: duct in air
        "AC":5,     # In asbestos cement: duct in concrete
        "GinP":6,   # Gas pressure cable in pipe                          
        "OinP":7,   # Oil pressure pipe-type cable 
        "PD":8,     # Plastic ducts
        }
    _error_code = []
    try:         ##Function style maintained in order to potentially consolidate into a future standardised function
        _group = 1
    except:
        ##no purpose##
        raise 
    if _group == 1:
        try:
            _row = _row_material[duct_material]
        except:
            print("Unexpected value or type for parameter 'duct_material'")
            raise
    U_constant = float(_table4.iloc[_row][2])
    V_constant = float(_table4.iloc[_row][3])
    Y_coefficient = float(_table4.iloc[_row][4])
    return(U_constant, V_constant, Y_coefficient, _error_code)

def formula2111(dc_conductor_diameter="", t1_insulation_thickness="", Pt_thermal_resistivity=""):
    """
    This FUNCTION applies to single core cables. It calculates the thermal resistance 'T1' between conductor and the cable's inner sheath. Typically this is the thermal resistance of the cable's conductor insulation layer. 'T1' is dependent on the insulation thickness, material thermal resistivity and conductor diameter.

    REQUIRED:
        **dc_conductor_diameter** (float [mm], None) - Diameter of conductor. IEC228.tableC1, C2 and C3 lists maximum and minimum conductor diameters for circular conductors. For shaped conductors the fictitious diameter can be calculated using formulas given in IEC60502.
        **t1_insulation_thickness** (float [mm], None) - Thickness of the insulation between conductor and sheath. IEC60502 carries a list of nominal thicknesses. Note, the tickness must include sheath bedding and other layers between conductor and sheath. For corrugated sheaths, the insulation thickness must be supplemented in order to account for material filling the interstitial spaces. #############Future, add sub-algorithms to calculate average PT, account for corrugated instances etc. Eg 'List' parameter for thickeneses and Pt's.
        **Pt_thermal_resistivity** (float [K.m/W], None) - Average thermal resistivity of the material between conductor and sheath. IEC60287_2_1.table1 lists values for common materials.

    OPTIONAL:

    OUTPUT:
        **T1_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T1, error_code = formula2111(3.5, 11.0)
    """

    _error_code = []
    PI=math.pi
    T1_thermal_resistance = (Pt_thermal_resistivity / (2 * PI)) * math.log(1 + (2 * t1_insulation_thickness / dc_conductor_diameter))
    return(T1_thermal_resistance, _error_code)

def formula2112(Pt_thermal_resistivity="", G_geometric_factor=""):
    """
    This FUNCTION applies to belted core cables. It calculates the thermal resistance 'T1' between a conductor and the cable's sheath. Typically this is the thermal resistance of the cable's insulation layers. 'T1' is dependent on the insulation thickness, material thermal resistivity and various construction geometries.

    REQUIRED:

        **Pt_thermal_resistivity** (float [K.m/W], None) - Average thermal resistivity of the material between conductor and sheath. IEC60287_2_1.table1 lists values for common materials.
        **G_geometric_factor** (float [K.m/W], None) - Geometric factor derived using functions formula21122-5.

    OPTIONAL:

    OUTPUT:
        **T1_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T1, error_code = formula2112(3.5, 11.0)
    """

    _error_code = []
    PI=math.pi
    T1_thermal_resistance = (Pt_thermal_resistivity / (2 * PI)) * G_geometric_factor)
    return(T1_thermal_resistance, _error_code)

def formula21121(): ########NEEDS TO BE DEVELOPED BECAUSE GRAPHS ARE INVOLVED
    return()

def formula21122(da_belt_diameter="", r1_radius_conductors="", dx_conductor_diameter="", t_insulation_thickness=""):

    """
    This FUNCTION applies to belted core cables. It returns the geometric factor 'G' for 2-Core, sector shaped conductor, belted cables. 'G' is dependent on the insulation thickness between conductors, insulation thickness between conductor and sheath, and diameter of the conductors.

    REQUIRED:
        **da_belt_diameter** (float [mm], None) - External diameter of the belt insulation.
        **r1_radius_conductors** (float [mm], None) - Radius of circle circumscribing conductors.
        **dx_conductor_diameter** (float [mm], None) - Fictitious diameter of conductor. For shaped conductors the fictitious diameter can be calculated using formulas given in IEC60502.
        **t_insulation_thickness** (float [mm], None) - Thickness of the insulation between conductors. IEC60502 carries a list of nominal thicknesses.

    OPTIONAL:

    OUTPUT:
        **G_geometric_factor** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        G = formula21122(11.0, 3.5, 2.0)
    """

    _error_code = []
    PI=math.pi
    _foo_ = 1 + (2.2 * t_insulation_thickness) / (2 * PI * (dx_conductor_diameter + t_insulation_thickness) - t_insulation_thickness)
    G_geometric_factor = 2 * _foo_ * math.log(da_belt_diameter / (2 * r1_radius_conductors))
    return(G_geometric_factor, _error_code)

def formula21123(): ########NEEDS TO BE DEVELOPED BECAUSE GRAPHS ARE INVOLVED
    return()

def formula21124(): ########NEEDS TO BE DEVELOPED BECAUSE GRAPHS ARE INVOLVED
    return()

def formula21125(da_belt_diameter="", r1_radius_conductors="", dx_conductor_diameter="", t_insulation_thickness=""):

    """
    This FUNCTION applies to belted core cables. It returns the geometric factor 'G' for 3-Core, sector shaped conductor, belted cables. 'G' is dependent on the insulation thickness between conductors, insulation thickness between conductor and sheath, and diameter of the conductors.

    REQUIRED:
        **da_belt_diameter** (float [mm], None) - External diameter of the belt insulation.
        **r1_radius_conductors** (float [mm], None) - Radius of circle circumscribing conductors.
        **dx_conductor_diameter** (float [mm], None) - Fictitious diameter of conductor. For shaped conductors the fictitious diameter can be calculated using formulas given in IEC60502.
        **t_insulation_thickness** (float [mm], None) - Thickness of the insulation between conductors. IEC60502 carries a list of nominal thicknesses.

    OPTIONAL:

    OUTPUT:
        **G_geometric_factor** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        G = formula21122(11.0, 3.5, 2.0)
    """

    _error_code = []
    PI=math.pi
    _foo_ = 1 + (3 * t_insulation_thickness) / (2 * PI * (dx_conductor_diameter + t_insulation_thickness) - t_insulation_thickness)
    G_geometric_factor = 2 * _foo_ * math.log(da_belt_diameter / (2 * r1_radius_conductors))
    return(G_geometric_factor, _error_code)

def formula21131(): ########NEEDS TO BE DEVELOPED BECAUSE GRAPHS ARE INVOLVED
    return()

def formula21132(): ########NEEDS TO BE DEVELOPED BECAUSE GRAPHS ARE INVOLVED
    return()

def formula21133(): ########NEEDS TO BE DEVELOPED BECAUSE GRAPHS ARE INVOLVED
    return()

def formula21141(dc_conductor_diameter="", ti_insulation_thickness="", Pt_thermal_resistivity=""):

    """
    This FUNCTION applies to Oil filled cables. The function calculates the thermal resistance 'T1' between a conductor and the cable's sheath for 3-core_circular conductor_metalised paper screen_with oil ducts cables. 'T1' is dependent on the insulation thickness, material thermal resistivity and various construction geometries.

    REQUIRED:
        **dc_conductor_diameter** (float [mm], None) - Diameter of conductor.
        **ti_insulation_thickness** (float [mm], None) - Thickness of the insulation between conductor and sheath. Note, the tickness must include sheath bedding and other layers between conductor and sheath. 
        **Pt_thermal_resistivity** (float [K.m/W], None) - Average thermal resistivity of the material between conductor and sheath. IEC60287_2_1.table1 lists values for common materials.

    OPTIONAL:

    OUTPUT:
        **T1_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T1, error_code = formula2111(3.5, 11.0)
    """

    _error_code = []
    T1_thermal_resistance = 0.358 * Pt_thermal_resistivity * ((2 * ti_insulation_thickness) / (dc_conductor_diameter + 2 * ti_insulation_thickness))
    return(T1_thermal_resistance, _error_code)

def formula21142(dc_conductor_diameter="", ti_insulation_thickness="", Pt_thermal_resistivity=""):

    """
    This FUNCTION applies to Oil filled cables. The function calculates the thermal resistance 'T1' between a conductor and the cable's sheath for 3-core_circular conductor_metal tape screen_with oil ducts cables. 'T1' is dependent on the insulation thickness, material thermal resistivity and various construction geometries.

    REQUIRED:
        **dc_conductor_diameter** (float [mm], None) - Diameter of conductor.
        **ti_insulation_thickness** (float [mm], None) - Thickness of the insulation between conductor and sheath. Note, the tickness must include sheath bedding and other layers between conductor and sheath. 
        **Pt_thermal_resistivity** (float [K.m/W], None) - Average thermal resistivity of the material between conductor and sheath. IEC60287_2_1.table1 lists values for common materials.

    OPTIONAL:

    OUTPUT:
        **T1_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T1, error_code = formula2111(3.5, 11.0)
    """

    _error_code = []
    T1_thermal_resistance = 0.358 * Pt_thermal_resistivity * (0.923 - dc_conductor_diameter / (dc_conductor_diameter + 2 * ti_insulation_thickness))
    return(T1_thermal_resistance, _error_code)

def formula21143(dc_conductor_diameter="", ti_insulation_thickness="", Pt_thermal_resistivity=""):

    """
    This FUNCTION applies to Oil filled cables. The function calculates the thermal resistance 'T1' between a conductor and the cable's sheath for 3-core_circular conductor_metalised paper screen_without oil ducts cables. 'T1' is dependent on the insulation thickness, material thermal resistivity and various construction geometries.

    REQUIRED:
        **dc_conductor_diameter** (float [mm], None) - Diameter of conductor.
        **ti_insulation_thickness** (float [mm], None) - Thickness of the insulation between conductor and sheath. Note, the tickness must include sheath bedding and other layers between conductor and sheath. 
        **Pt_thermal_resistivity** (float [K.m/W], None) - Average thermal resistivity of the material between conductor and sheath. IEC60287_2_1.table1 lists values for common materials.

    OPTIONAL:

    OUTPUT:
        **T1_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T1, error_code = formula2111(3.5, 11.0)
    """
######## Formula is right but need to assign correct variable names
    _error_code = []
    _tg_ = 0.5 * ((Dit + Dic) / 2) - 2.16 * Dc)
    T1_thermal_resistance = (475 / Dc ** 1.74) * (_tg_ / Dc) ** 0.62 + (Pt / (2 * PI)) * math.log((Dc - 2 * delta1) / dc)
    return(T1_thermal_resistance, _error_code)

def formula2121(ds_sheath_diameter="", t2_bedding_thickness="", Pt_thermal_resistivity=""):
    """
    This FUNCTION applies to single core cables. It calculates the thermal resistance 'T2' between sheath and armour. Typically this is the thermal resistance of the cable's bedding layer. 'T2' is dependent on the insulation thickness, material thermal resistivity and sheath diameter.

    REQUIRED:
        **ds_sheath_diameter** (float [mm], None) - External diameter of the sheath.
        **t2_bedding_thickness** (float [mm], None) - Thickness of the bedding.
        **Pt_thermal_resistivity** (float [K.m/W], None) - Average thermal resistivity of the material between conductor and sheath. IEC60287_2_1.table1 lists values for common materials.

    OPTIONAL:

    OUTPUT:
        **T2_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T2, error_code = formula2111(3.5, 11.0)
    """

    _error_code = []
    PI=math.pi
    T2_thermal_resistance = (1 / (2 * PI)) * Pt_thermal_resistivity * math.log(1 + (2 * t2_bedding_thickness) / ds_sheath_diameter)
    return(T2_thermal_resistance, _error_code)

def formula2122(): ########NEEDS TO BE DEVELOPED BECAUSE GRAPHS ARE INVOLVED
    return()

def formula213(): ########NEEDS TO BE DEVELOPED BECAUSE corrugated sheths are involved. it is easy though. im just lazy and it is late
    return()

###################################################################################
def formula2211(De_cable_diameter="", Z_coefficent="", E_constant="", g_coefficent="", lambda1_ratio="", lambda2_ratio="", T1_thermal_resistance="", T2_thermal_resistance="", T3_thermal_resistance="", dTheta_kelvin="", n_conductor_count="", Wd_watt_per_meter=""):
    """
    This FUNCTION calculates the thermal resistance 'T4' of the cable surrounds in air. 'T4' is dependent on the cable diameter.

    REQUIRED:
        **De_cable_diameter** (float [mm], None) - External diameter of the cable. Note, for cables with corrugated sheaths DE must be ammended using the specified formula.
        **Z_coefficent** (float [mm], None) - Coefficient derived from table2.
        **E_constant** (float [mm], None) - Value derived from table2
        **g_coefficent** (float [mm], None) - Value derived from table2
        **lambda1_ratio** (float [mm], None) - 
        **lambda2_ratio** (float [mm], None) - 
        **T1_thermal_resistance** (float [mm], None) - 
        **T2_thermal_resistance** (float [mm], None) - 
        **T3_thermal_resistance** (float [mm], None) - 
        **dTheta_kelvin** (float [mm], None) - 
        **n_conductor_count** (float [mm], None) - 
        **Wd_watt_per_meter** (float [mm], None) - 

    OPTIONAL:

    OUTPUT:
        **T4_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T4, error_code = formula2111(3.5, 11.0)
    """

    _error_code = []
    PI=math.pi
    _h_ = (Z_coefficent * 1000 / De_cable_diameter ** g_coefficent) + E_constant
    delta_theta_d = Wd_watt_per_meter * ((1/(1+ lambda1_ratio + lambda2_ratio) - 0.5) * T1_thermal_resistance - (n_conductor_count * lambda2_ratio * T2_thermal_resistance) / (1 + lambda1_ratio + lambda2_ratio))
    _KA_ = (PI * De_cable_diameter * _h_ / (1 + lambda1_ratio + lambda2_ratio)) * (T1_thermal_resistance / n_conductor_count + T2_thermal_resistance * (1+lambda1_ratio) + T3_thermal_resistance * (1 + lambda1_ratio + lambda2_ratio))

    while _foo_ > 0.001:
        _foo_plus_one = ((dTheta_kelvin + delta_theta_d) / (1 + _KA_ * _foo_))
        _foo_ = _foo_plus_one

    delta_theta_s = _foo_ ** 4


    T4_thermal_resistance = (1000 / (math.pi * De_cable_diameter * _h_ * (delta_theta_s) ** 0.25))
    return(T2_thermal_resistance, _error_code)

def formula2212(De_cable_diameter="", Z_coefficent="", E_constant="", g_coefficent="", lambda1_ratio="", lambda2_ratio="", T1_thermal_resistance="", T2_thermal_resistance="", T3_thermal_resistance="", dTheta_kelvin="", n_conductor_count="", Wd_watt_per_meter="", rho="", H_solar_radiation=1000):
    """
    This FUNCTION calculates the thermal resistance 'T4' of the cable surrounds in air. 'T4' is dependent on the cable diameter.

    REQUIRED:
        **De_cable_diameter** (float [mm], None) - External diameter of the cable. Note, for cables with corrugated sheaths DE must be ammended using the specified formula.
        **Z_coefficent** (float [mm], None) - Coefficient derived from table2.
        **E_constant** (float [mm], None) - Value derived from table2
        **g_coefficent** (float [mm], None) - Value derived from table2
        **lambda1_ratio** (float [mm], None) - 
        **lambda2_ratio** (float [mm], None) - 
        **T1_thermal_resistance** (float [mm], None) - 
        **T2_thermal_resistance** (float [mm], None) - 
        **T3_thermal_resistance** (float [mm], None) - 
        **dTheta_kelvin** (float [mm], None) - 
        **n_conductor_count** (float [mm], None) - 
        **Wd_watt_per_meter** (float [mm], None) - 
        **H** (float [mm], 1000) -

    OPTIONAL:

    OUTPUT:
        **T4_thermal_resistance** (float) 
    
    ERROR:
        **_error_code** - '0' Parameter out of range. No value given.

    EXAMPLE:
        T4, error_code = formula2111(3.5, 11.0)
    """

    _error_code = []
    PI=math.pi
    _h_ = (Z_coefficent * 1000 / De_cable_diameter ** g_coefficent) + E_constant
    delta_theta_d = Wd_watt_per_meter * ((1/(1+ lambda1_ratio + lambda2_ratio) - 0.5) * T1_thermal_resistance - (n_conductor_count * lambda2_ratio * T2_thermal_resistance) / (1 + lambda1_ratio + lambda2_ratio))
    delta_theta_ds = (rho * De_cable_diameter * H_solar_radiation) * (T1_thermal_resistance/n_conductor_count + T2_thermal_resistance*(1+lambda1_ratio) + T3_thermal_resistance(1+lambda1_ratio+lambda2_ratio)/(1000*(1+lambda1_ratio+lambda2_ratio)))
    _KA_ = (PI * De_cable_diameter * _h_ / (1 + lambda1_ratio + lambda2_ratio)) * (T1_thermal_resistance / n_conductor_count + T2_thermal_resistance * (1+lambda1_ratio) + T3_thermal_resistance * (1 + lambda1_ratio + lambda2_ratio))

    while _foo_ > 0.001:
        _foo_plus_one = ((dTheta_kelvin + delta_theta_d + delta_theta_ds) / (1 + _KA_ * _foo_))
        _foo_ = _foo_plus_one

    delta_theta_s = _foo_ ** 4


    T4_thermal_resistance = (1000 / (math.pi * De_cable_diameter * _h_ * (delta_theta_s) ** 0.25))
    return(T2_thermal_resistance, _error_code)

        