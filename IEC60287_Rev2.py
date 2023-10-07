#Formulas
import IEC60228
import IEC60287_2_1
#Tables
import pandas as pd
with pd.ExcelFile("D:\Carlos_Cloud Folders\OneDrive\JupyterProjects\IEC\IEC60287.xlsx") as iec_table:
#with pd.ExcelFile("C:\Users\Carlos\OneDrive\JupyterProjects\IEC\IEC60287.xlsx") as iec_table:
    _table1 = pd.read_excel(iec_table, "table1", skiprows=3, dtype='str', header=None, names=[1,2,3,4])
    _table2 = pd.read_excel(iec_table, "table2", skiprows=3, dtype='str', header=None, names=[1,2,3,4,5,6,7,8,9,10])
    _table3 = pd.read_excel(iec_table, "table3", skiprows=4, dtype='str', header=None, names=[1,2,3,4])
    _table4 = pd.read_excel(iec_table, "table4", skiprows=3, dtype='str', header=None, names=[1,2,3,4])
    
def table1(metal="none", conductor="yes"):
    try:
        if {"yes":"y", "no":"n"}[conductor]=="y":
            try:
                _row={"copper":0,
                      "aluminium":1,
                      "none":"nan"
                     }[metal]
            except:
                raise
        else:
            try:
                _row={"lead":2, 
                      "steel":3, 
                      "bronze":"4", 
                      "stainless":"5", 
                      "aluminium":"6", 
                      "none":"nan"
                     }[metal]
            except:
                raise
    except:
        raise 
    if _row=="nan":
        return("nan","nan")
    return(float(_table1.iloc[_row][3]),float(_table1.iloc[_row][4]))

def table2(conductor="none", shape="none", arrangement="none", insulation="extruded"):
    try:
        if {"copper":"Cu", "Al":"Al"}[conductor]=="Cu":
            if {"round":"round", "sector":"sector", "hollow":"hollow"}[shape]=="round":
                try:
                    _row={"solid":{"all":0, "none":0}, 
                          "stranded":{"fluid":1, "paper":1, "PPL":1, "none":"nan"},
                          "stranded":{"extruded":2, "mineral":2, "none":"nan"},
                          "milliken":{"fluid":3, "paper":3, "PPL":3, "none":"nan"},
                          "milliken-insulated":{"extruded":4, "none":"nan"},
                          "milliken-bare-unidirect":{"extruded":5, "none":"nan"},
                          "milliken-bare-bidirect":{"extruded":6, "none":"nan"}
                         }[arrangement][insulation]
                except:
                    raise
            elif {"round":"round", "sector":"sector", "hollow":"hollow"}[shape]=="sector":
                try:
                    _row={"fluid":8, 
                          "paper":8, 
                          "PPL":89, 
                          "extruded":9, 
                          "mineral":9, 
                          "none":"nan"
                         }[insulation]
                except:
                    raise        
            else:
                _row=8
        else:
            if {"round":"round", "hollow":"hollow"}[shape]=="round":
                try:
                    _row={"solid":10, 
                          "stranded":11,
                          "milliken":12
                         }[arrangement]
                except:
                    raise
            else:
                _row=14        
    except:
        raise 
    if _row=="nan":
        return("nan","nan")
    return(float(_table2.iloc[_row][4]),float(_table2.iloc[_row][5]))

def table3(insulation="none", type="none"):
    try:
        if {"paper":"paper", "other":"other"}[insulation]=="paper":
            try:
                _row={"t1":0,
                      "t2":1,
                      "t3":2,
                      "t4":3,
                      "t5":4,
                      "t6":5,
                      "t7":6,
                      "t8":7
                     }[type]
            except:
                raise
        else:
            try:
                _row={"t1":8,
                      "t2":9,
                      "t3":10,
                      "t4":11,
                      "t5":12,
                      "t6":13,
                      "t7":14,
                      "t8":15
                     }[type]
            except:
                raise       
    except:
        raise 
    if _row=="nan":
        return("nan","nan")
    return(float(_table3.iloc[_row][3]),float(_table3.iloc[_row][4]))

def table4(insulation="none"):
    try:
        _row={"bitumen":0,
              "jute":1,
              "polychloroprene":2,
              "neoprene":2,
              "pvc":3,
              "pe":4,
              "lead":5,
              }[insulation]
    except:
        raise 
    if _row=="nan":
        return("nan")
    return(float(_table4.iloc[_row][2]))

def formula1411(I_conductor_amp="none", dTheta_kelvin="none", Rac_conductor_ohm_per_meter="none", Wd_watt_per_meter="none", T1_kelvin_meter_per_watt="none", T2_kelvin_meter_per_watt="none", T3_kelvin_meter_per_watt="none", T4_kelvin_meter_per_watt="none", n_conductor_count="none", lambda1_ratio="none", lambda2_ratio="none"):
    # TITLE: Permissable Current Rating: Buried cables where drying out of the soil does not occur or cables in air_AC cables
    dTheta_permissable_kelvin=(I_conductor_amp**2 * Rac_conductor_ohm_per_meter + 0.5 * Wd_watt_per_meter) * T1_kelvin_meter_per_watt+(I_conductor_amp**2 * Rac_conductor_ohm_per_meter * ( 1 + lambda1_ratio ) + Wd_watt_per_meter ) * n_conductor_count * T2_kelvin_meter_per_watt + ( I_conductor_amp**2 * Rac_conductor_ohm_per_meter * (1 + lambda1_ratio + lambda2_ratio) + Wd_watt_per_meter)* n_conductor_count  * (T3_kelvin_meter_per_watt + T4_kelvin_meter_per_watt)
    I_permissable_conductor_amp=((dTheta_kelvin-Wd_watt_per_meter*(0.5*T1_kelvin_meter_per_watt+n_conductor_count*(T2_kelvin_meter_per_watt+T3_kelvin_meter_per_watt+T4_kelvin_meter_per_watt)))/(Rac_conductor_ohm_per_meter*T1_kelvin_meter_per_watt+n_conductor_count*Rac_conductor_ohm_per_meter*(1+lambda1_ratio)*T2_kelvin_meter_per_watt+n_conductor_count*Rac_conductor_ohm_per_meter*(1+lambda1_ratio+lambda2_ratio)*(T3_kelvin_meter_per_watt+T4_kelvin_meter_per_watt)))**0.5

    return(I_permissable_conductor_amp,dTheta_permissable_kelvin)

def formula1412(I_conductor_amp="none", dTheta_kelvin="none", Rdc_conductor_ohm_per_meter="none", Wd_watt_per_meter="none", R="none", T1_kelvin_meter_per_watt="none", T2_kelvin_meter_per_watt="none", T3_kelvin_meter_per_watt="none", T4_kelvin_meter_per_watt="none", n_conductor_count="none"):
    # TITLE: Permissable Current Rating: Buried cables where drying out of the soil does not occur or cables in air: DC cables up to 5kV
    dTheta_permissable_kelvin=(I_conductor_amp**2*Rdc_conductor_ohm_per_meter)*T1_kelvin_meter_per_watt+I_conductor_amp**2*Rdc_conductor_ohm_per_meter*n_conductor_count*T2_kelvin_meter_per_watt+I_conductor_amp**2*Rdc_conductor_ohm_per_meter*n_conductor_count*(T3_kelvin_meter_per_watt+T4_kelvin_meter_per_watt)
    I_permissable_conductor_amp=(dTheta_kelvin/(Rdc_conductor_ohm_per_meter*T1_kelvin_meter_per_watt+n_conductor_count*Rdc_conductor_ohm_per_meter*T2_kelvin_meter_per_watt+n_conductor_count*Rdc_conductor_ohm_per_meter*(T3_kelvin_meter_per_watt+T4_kelvin_meter_per_watt)))**0.5
    return(I_permissable_conductor_amp)

def formula1421(I_conductor_amp="none", dTheta_kelvin="none", Rac_conductor_ohm_per_meter="none", Wd_watt_per_meter="none", T1_kelvin_meter_per_watt="none", T2_kelvin_meter_per_watt="none", T3_kelvin_meter_per_watt="none", T4_kelvin_meter_per_watt="none", n_conductor_count="none", lambda1_ratio="none", lambda2_ratio="none", dTheta_kelvin_x="none", Pd_dry_soil_thermal_resistivity="none", Pw_moist_soil_thermal_resistivity="none"):
    # TITLE: Permissable Current Rating: Buried cables where drying out of the soil does occur: AC cables
    v_dry_moist_ratio = Pd_dry_soil_thermal_resistivity/Pw_moist_soil_thermal_resistivity
    I_permissable_conductor_amp=((dTheta_kelvin-Wd_watt_per_meter*(0.5*T1_kelvin_meter_per_watt+n_conductor_count*(T2_kelvin_meter_per_watt+T3_kelvin_meter_per_watt+v_dry_moist_ratio*T4_kelvin_meter_per_watt))+(v_dry_moist_ratio-1)*dTheta_kelvin_x)/(Rac_conductor_ohm_per_meter*T1_kelvin_meter_per_watt+n_conductor_count*Rac_conductor_ohm_per_meter*(1+lambda1_ratio)*T2_kelvin_meter_per_watt+n_conductor_count*Rac_conductor_ohm_per_meter*(1+lambda1_ratio+lambda2_ratio)*(T3_kelvin_meter_per_watt+v_dry_moist_ratio*T4_kelvin_meter_per_watt)))**0.5
    return(I_permissable_conductor_amp)

def formula1422(I_conductor_amp="none", dTheta_kelvin="none", Rdc_conductor_ohm_per_meter="none", Wd_watt_per_meter="none", R="none", T1_kelvin_meter_per_watt="none", T2_kelvin_meter_per_watt="none", T3_kelvin_meter_per_watt="none", T4_kelvin_meter_per_watt="none", n_conductor_count="none", dTheta_kelvin_x="none", Pd_dry_soil_thermal_resistivity="none", Pw_moist_soil_thermal_resistivity="none"):
    # TITLE: Permissable Current Rating: Buried cables where drying out of the soil does occur: DC cables up to 5kV
    v_dry_moist_ratio = Pd_dry_soil_thermal_resistivity/Pw_moist_soil_thermal_resistivity
    I_permissable_conductor_amp=((dTheta_kelvin+(v_dry_moist_ratio-1)*dTheta_kelvin_x/(Rdc_conductor_ohm_per_meter*T1_kelvin_meter_per_watt+n_conductor_count*Rdc_conductor_ohm_per_meter*T2_kelvin_meter_per_watt+n_conductor_count*Rdc_conductor_ohm_per_meter*(T3_kelvin_meter_per_watt+v_dry_moist_ratio*T4_kelvin_meter_per_watt))))**0.5
    return(I_permissable_conductor_amp)

def formula1431(I_conductor_amp="none", dTheta_kelvin="none", Rac_conductor_ohm_per_meter="none", Wd_watt_per_meter="none", T1_kelvin_meter_per_watt="none", T2_kelvin_meter_per_watt="none", T3_kelvin_meter_per_watt="none", T4_kelvin_meter_per_watt="none", n_conductor_count="none", lambda1_ratio="none",lambda2_ratio="none", dTheta_kelvin_x="none"):
    # TITLE: Permissable Current Rating: Buried cables where drying out of the soil is to be avoided: AC cables
    I_permissable_conductor_amp=((dTheta_kelvin_x-n_conductor_count*Wd_watt_per_meter*T4_kelvin_meter_per_watt)/(n_conductor_count*Rac_conductor_ohm_per_meter*T4_kelvin_meter_per_watt*(1+lambda1_ratio+lambda2_ratio)))**0.5
    return(I_permissable_conductor_amp)

def formula1432(dTheta_kelvin="none", Wd_watt_per_meter="none", Rdc_conductor_ohm_per_meter="none", T1_kelvin_meter_per_watt="none", T2_kelvin_meter_per_watt="none", T3_kelvin_meter_per_watt="none", T4_kelvin_meter_per_watt="none", n_conductor_count="none", lambda1_ratio="none", lambda2_ratio="none", dTheta_kelvin_x="none"):
    # TITLE: Permissable Current Rating: Buried cables where drying out of the soil is to be avoided: DC cables up to 5kV
    I_permissable_conductor_amp=((dTheta_kelvin_x)/(n_conductor_count*Rdc_conductor_ohm_per_meter*T4_kelvin_meter_per_watt))**0.5
    return(I_permissable_conductor_amp)

def formula21(Rdc_conductor_ohm_per_meter="none", Ys_skin_effect="none", Yp_proximity_effect="none"):
    # TITLE: AC Resistance of conductor
    Rac_conductor_ohm_per_meter=Rdc_conductor_ohm_per_meter*(1+Ys_skin_effect+Yp_proximity_effect)
    return(Rac_conductor_ohm_per_meter)

def formula211(R0="none", alpha20="none", theta="none"):
    # TITLE: DC Resistance of conductor @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Rdc_conductor_ohm_per_meter=R0*(1+alpha20*(theta-20))
    return(Rdc_conductor_ohm_per_meter)

def formula212(Rdc_conductor_ohm_per_meter="none", ks_table_2="none", f_hz=50):
    #TITLE: Skin effect factor
    PI=3.141592653589793
    Xs_bessel_factor_for_skin_effect=((8*PI*f_hz*1E-7*ks_table_2)/Rdc_conductor_ohm_per_meter)**0.5
    if Xs_bessel_factor_for_skin_effect<=2.8:
        Ys_skin_effect_factor=Xs_bessel_factor_for_skin_effect**4/(192+0.8*Xs_bessel_factor_for_skin_effect**4)
    elif Xs_bessel_factor_for_skin_effect<=3.8:
        Ys_skin_effect_factor=-0.136-0.0177*Xs_bessel_factor_for_skin_effect+0.0563*Xs_bessel_factor_for_skin_effect**2
    else:
        Ys_skin_effect_factor=0.354*Xs_bessel_factor_for_skin_effect-0.733
    return(Ys_skin_effect_factor)

def formula213(Rdc_conductor_ohm_per_meter="none", kp_table_2="none", f_hz=50, dc_conductor_diameter_mm="none", s_conductor_spacing_mm="none"):
    #TITLE: Proximity effect factor: For two core cables and two single core cables
    PI=3.141592653589793
    Xp_bessel_factor_for_proximity_effect=((8*PI*f_hz*1E-7*kp_table_2)/Rdc_conductor_ohm_per_meter)**0.5
    Yp_proximity_effect=(Xp_bessel_factor_for_proximity_effect**4/(192+0.8*Xp_bessel_factor_for_proximity_effect**4))*2.9*(dc_conductor_diameter_mm/s_conductor_spacing_mm)**2
    return(Yp_proximity_effect)

def formula2141(Rdc_conductor_ohm_per_meter="none", kp_table_2="none", f_hz="none", dc_conductor_diameter_mm="none", s_conductor_spacing_mm="none"):
    #TITLE: Proximity effect factor: For three core cables and three single core cables
    PI=3.141592653589793
    Xp_bessel_factor_for_proximity_effect=((8*PI*f_hz*1E-7*kp_table_2)/Rdc_conductor_ohm_per_meter)**0.5
    Yp_proximity_effect=(Xp_bessel_factor_for_proximity_effect**4/(192+0.8*Xp_bessel_factor_for_proximity_effect**4))*(dc_conductor_diameter_mm/s_conductor_spacing_mm)**2*(0.312*(dc_conductor_diameter_mm/s_conductor_spacing_mm)**2+1.18/((Xp_bessel_factor_for_proximity_effect**4/(192+0.8*Xp_bessel_factor_for_proximity_effect**4))+0.27))
    return(Yp_proximity_effect)

def formula2142(Rdc_conductor_ohm_per_meter="none", kp_table_2="none", f_hz="none", dx_conductor_diameter_mm="none", s_conductor_spacing_mm="none"):
    #TITLE: Proximity effect factor: For multicore core cables with shaped conductors
    PI=3.141592653589793 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
    Xp_bessel_factor_for_proximity_effect=((8*PI*f_hz*1E-7*kp_table_2)/Rdc_conductor_ohm_per_meter)**0.5
    Yp_proximity_effect=(2/3)*(Xp_bessel_factor_for_proximity_effect**4/(192+0.8*Xp_bessel_factor_for_proximity_effect**4))*(dx_conductor_diameter_mm/s_conductor_spacing_mm)**2*(0.312*(dx_conductor_diameter_mm/s_conductor_spacing_mm)**2+1.18/((Xp_bessel_factor_for_proximity_effect**4/(192+0.8*Xp_bessel_factor_for_proximity_effect**4))+0.27))
    return(Yp_proximity_effect)

def formula215(Rdc_conductor_ohm_per_meter="none", Yp_proximity_effect="none", Ys_skin_effect_factor="none"):
    #TITLE: Skin and Proximity effect factor for pipe-type cables
    Rac_conductor_ohm_per_meter=Rdc_conductor_ohm_per_meter*(1+1.5*(Ys_skin_effect_factor+Yp_proximity_effect))
    return(Rac_conductor_ohm_per_meter)

def formula22(U0_volt_to_earth="none", epsilon_table_3="none", TanDelta_table_3="none", Di_insulation_outside_diameter_mm="none", dc_conductor_diameter_mm="none",f_hz="none"):
    #TITLE: Dielectric losses (applies to AC cables only)
    PI=3.141592653589793
    C_capacitance_per_meter=(epsilon_table_3*1E-9)/(18*1E10*(((Di_insulation_outside_diameter_mm/dc_conductor_diameter_mm)**(1/1E10))-1)) #@@@@@@
    Wd_watt_per_meter= 2 * PI * f_hz * C_capacitance_per_meter * U0_volt_to_earth**2 * TanDelta_table_3
    return(Wd_watt_per_meter)

def current_capacity(project, from_terminal, to_terminal, length_m, conductor_strand_count, conductor_strand_diameter, conductor_nominal_diameter, conductor_insulation_thickness, conductor_insulation_material, conductor_metal, conductor_construction_type, cable_innerCovering_thickness, cable_innerCovering_material, cable_innerCovering_diameter, cable_metalSheath_thickess, cable_metalSheath_material, cable_seperationSheath_thickness, cable_seperationSheath_material, cable_armourTape_thickness, cable_armourWire_diameter, cable_overSheath_thickness, cable_overSheath_material, cable_overSheath_diameter, n_conductor_count, f_hz="none"):
    #TITLE: Determine max current capacity of cable
    #First conductor resistance is required. Using conductor strands.....
    PI=3.141592653589793
    #Calculate losses:
    #DC Resistance at max temperature
    conductor_area = conductor_strand_count * PI * ( conductor_strand_diameter / 2 )**2
    conductor_resistivity, alpha20 = table1(metal=conductor_metal, conductor="yes")
    R0 = conductor_resistivity * 1000**2 / conductor_area
    theta = 70 ####need to get max temps for insulation
    Rdc_max = formula211(R0, alpha20, theta)
    #Skin and Proximity effect factor
    ks, kp = table2(conductor=conductor_metal, shape="sector", arrangement="stranded", insulation="extruded") ##wrong table variables
    s_conductor_spacing_mm = conductor_nominal_diameter + 2 * conductor_insulation_thickness
    Ys = formula212(Rdc_conductor_ohm_per_meter=Rdc_max, ks_table_2=ks, f_hz=50)
    Yp = formula2141(Rdc_conductor_ohm_per_meter=Rdc_max, kp_table_2=kp, f_hz=50, dc_conductor_diameter_mm=conductor_nominal_diameter, s_conductor_spacing_mm=5 ) ##assuming three core round condcutor for now
    #Total losses
    Rac_max = formula21(Rdc_conductor_ohm_per_meter=Rdc_max, Ys_skin_effect=Ys, Yp_proximity_effect=Yp)
    #Dielectirc losses
    ##Not calculated for now as it only applies to MV cables
    Wd_watt_per_meter = 0
    #T1 thermal resistance of insulation
    T1_kelvin_meter_per_watt = IEC60287_2_1.formula2111(conductor_construction_type=conductor_construction_type, conductor_insulation_thickness=conductor_insulation_thickness, conductor_nominal_diameter=conductor_nominal_diameter, conductor_insulation_material=conductor_insulation_material)
    #T2 thermal resistance of sheath
    T2_kelvin_meter_per_watt = IEC60287_2_1.formula2121(cable_innerCovering_thickness=cable_innerCovering_thickness, cable_innerCovering_diameter=cable_innerCovering_diameter, cable_innerCovering_material=cable_innerCovering_material, conductor_construction_type=conductor_construction_type)
    #T3 thermal resistance of sheath
    T3_kelvin_meter_per_watt = IEC60287_2_1.formula213(cable_overSheath_thickness=cable_overSheath_thickness, cable_overSheath_diameter=cable_overSheath_diameter, cable_overSheath_material=cable_overSheath_material, conductor_construction_type=conductor_construction_type)
    ###Makinng Lambda1 and lambda2 = 0
    lambda1_ratio = 0
    lambda2_ratio = 0
    #Calculate maximum current
    I_permissable_conductor_amp,dTheta_permissable_kelvin = formula1411(I_conductor_amp=1, dTheta_kelvin=45, Rac_conductor_ohm_per_meter=Rac_max, Wd_watt_per_meter=Wd_watt_per_meter, T1_kelvin_meter_per_watt=T1_kelvin_meter_per_watt, T2_kelvin_meter_per_watt=T2_kelvin_meter_per_watt, T3_kelvin_meter_per_watt=T3_kelvin_meter_per_watt, T4_kelvin_meter_per_watt=0, n_conductor_count=n_conductor_count, lambda1_ratio=lambda1_ratio, lambda2_ratio=lambda2_ratio) 
    return(I_permissable_conductor_amp,dTheta_permissable_kelvin)


print(IEC60228.table1(csa="6", conductor="Cu", type="plain"))

project="none"
from_terminal="none"
to_terminal="none"
length_m=100
conductor_strand_count=95
conductor_strand_diameter=1
conductor_nominal_diameter=20
conductor_insulation_thickness=1
conductor_insulation_material="PVC"
conductor_metal="copper"
conductor_construction_type="4C"
cable_innerCovering_thickness=1
cable_innerCovering_material="PVC"
cable_innerCovering_diameter=40
cable_metalSheath_thickess=1
cable_metalSheath_material="Lead"
cable_seperationSheath_thickness=1
cable_seperationSheath_material="PVC"
cable_armourTape_thickness=1
cable_armourWire_diameter=2.5
cable_overSheath_thickness=1
cable_overSheath_material="PVC"
cable_overSheath_diameter=1
n_conductor_count=4
f_hz=50
x,y=current_capacity(project, from_terminal, to_terminal, length_m, conductor_strand_count, conductor_strand_diameter, conductor_nominal_diameter, conductor_insulation_thickness, conductor_insulation_material, conductor_metal, conductor_construction_type, cable_innerCovering_thickness, cable_innerCovering_material, cable_innerCovering_diameter, cable_metalSheath_thickess, cable_metalSheath_material, cable_seperationSheath_thickness, cable_seperationSheath_material, cable_armourTape_thickness, cable_armourWire_diameter, cable_overSheath_thickness, cable_overSheath_material, cable_overSheath_diameter, n_conductor_count, f_hz="none")
print(x,y)