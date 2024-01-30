import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import base64
from io import BytesIO
def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph
def cons(x,y,z):
    plt.switch_backend('AGG')


        # Définition des antécédents et des conséquents
    grippe = ctrl.Antecedent(np.arange(1, 100, 2), 'grippe')
    palu = ctrl.Antecedent(np.arange(1, 30, 1), 'palu')
    omicron = ctrl.Antecedent(np.arange(0, 6, 0.1), 'omicron')

    prescription = ctrl.Consequent(np.arange(1, 100, 1), 'prescription')
    laborantin = ctrl.Consequent(np.arange(1, 100, 1), 'laborantin')

    #fig, axes = plt.subplots(2, 3, figsize=(15, 8))

    #fig = plt.figure(layout="constrained")
    fig = plt.figure(figsize=(12, 8))

    subfigs = fig.subfigures(1, 2, wspace=0.07, width_ratios=[1.5, 1.])
    axes_a = subfigs[0].subplots(2, 2)
    subfigs[0].set_facecolor('lightblue')
    subfigs[0].suptitle('Antecedents')
    #subfigs[0].supxlabel('xlabel for subfigs[0]')

    axes_c = subfigs[1].subplots(2, 1)
    subfigs[1].suptitle('Consequences')
    #subfigs[1].supylabel('ylabel for subfigs[1]')

    # Définition des ensembles flous avec trapmf pour "grippe"
    toux_faible = fuzz.trapmf(grippe.universe, [1, 1, 30, 45])  # Définition de l'ensemble "toux_faible" avec trapmf
    grippe['toux_faible'] = toux_faible  # Attribution de l'ensemble défini à la variable "grippe"
    rhume = fuzz.trapmf(grippe.universe, [20, 20, 70, 70])  # Définition de l'ensemble "rhume" avec trapmf
    grippe['rhume'] = rhume  # Attribution de l'ensemble défini à la variable "grippe"
    toux_fort = fuzz.trapmf(grippe.universe, [45, 45, 100, 100])  # Définition de l'ensemble "toux_fort" avec trapmf
    grippe['toux_fort'] = toux_fort  # Attribution de l'ensemble défini à la variable "grippe"

    # Définition des ensembles flous avec trapmf pour "palu"
    dm_fort = fuzz.trapmf(palu.universe, [12, 12, 30, 30])  # Définition de l'ensemble "dm_fort" avec trapmf
    palu['dm_fort'] = dm_fort  # Attribution de l'ensemble défini à la variable "palu"
    dm_moyenne = fuzz.trapmf(palu.universe, [8, 8, 15, 15])  # Définition de l'ensemble "dm_moyenne" avec trapmf
    palu['dm_moyenne'] = dm_moyenne  # Attribution de l'ensemble défini à la variable "palu"
    dm_leger = fuzz.trapmf(palu.universe, [1, 1, 10, 10])  # Définition de l'ensemble "dm_leger" avec trapmf
    palu['dm_leger'] = dm_leger  # Attribution de l'ensemble défini à la variable "palu"

    # Définition des ensembles flous avec trapmf pour "omicron"
    pt_appetit = fuzz.trapmf(omicron.universe, [0, 0, 2, 2])  # Définition de l'ensemble "pt_appetit" avec trapmf
    omicron['pt_appetit'] = pt_appetit  # Attribution de l'ensemble défini à la variable "omicron"
    pm_appetit = fuzz.trapmf(omicron.universe, [1, 1, 4, 4])  # Définition de l'ensemble "pm_appetit" avec trapmf
    omicron['pm_appetit'] = pm_appetit  # Attribution de l'ensemble défini à la variable "omicron"
    sp_appetit = fuzz.trapmf(omicron.universe, [2, 2, 6, 6])  # Définition de l'ensemble "sp_appetit" avec trapmf
    omicron['sp_appetit'] = sp_appetit  # Attribution de l'ensemble défini à la variable "omicron"

    # Définition des ensembles flous avec trapmf pour "prescription"
    sur_rv = fuzz.trapmf(prescription.universe, [1, 1, 50, 50])  # Définition de l'ensemble "sur_rv" avec trapmf
    prescription['sur_rv'] = sur_rv  # Attribution de l'ensemble défini à la variable "prescription"
    via_l_appli = fuzz.trapmf(prescription.universe, [40, 40, 100, 100])  # Définition de l'ensemble "via_l_appli" avec trapmf
    prescription['via_l_appli'] = via_l_appli  # Attribution de l'ensemble défini à la variable "prescription"

    # Définition des ensembles flous avec trapmf pour "laborantin"
    bilan = fuzz.trapmf(laborantin.universe, [1, 1, 30, 30])  # Définition de l'ensemble "bilan" avec trapmf
    laborantin['bilan'] = bilan  # Attribution de l'ensemble défini à la variable "laborantin"
    test = fuzz.trapmf(laborantin.universe, [30, 30, 70, 70])  # Définition de l'ensemble "test" avec trapmf
    laborantin['test'] = test  # Attribution de l'ensemble défini à la variable "laborantin"
    scan = fuzz.trapmf(laborantin.universe, [80, 80, 100, 100])  # Définition de l'ensemble "scan" avec trapmf
    laborantin['scan'] = scan  # Attribution de l'ensemble défini à la variable "laborantin"

    # Affichage des ensembles flous
    axes_a[0,0].plot(grippe.universe, toux_faible, 'b',linewidth=1.5, label='Toux faible')
    axes_a[0,0].plot(grippe.universe, rhume, 'g', linewidth=1.5,label='Rhume')
    axes_a[0,0].plot(grippe.universe, toux_fort, 'r',linewidth=1.5, label='Toux fort')
    axes_a[0,0].set_title('Grippe saisonnière')
    axes_a[0,0].legend()

    axes_a[0,1].plot(palu.universe, dm_fort, 'b', linewidth=1.5,label='DM Fort')
    axes_a[0,1].plot(palu.universe, dm_moyenne, 'g',linewidth=1.5, label='DM Moyenne')
    axes_a[0,1].plot(palu.universe, dm_leger, 'r', linewidth=1.5,label='DM Leger')
    axes_a[0,1].set_title('Douleur Musculaire')
    axes_a[0,1].legend()

    axes_a[1,1].plot(omicron.universe, pt_appetit, 'b', linewidth=1.5,label='PT Appetit')
    axes_a[1,1].plot(omicron.universe, pm_appetit, 'g', linewidth=1.5,label='PM Appetit')
    axes_a[1,1].plot(omicron.universe, sp_appetit, 'r',linewidth=1.5, label='SP Appetit')
    axes_a[1,1].set_title('Appetit (Degust)')
    axes_a[1,1].legend()

    axes_c[0].plot(prescription.universe, sur_rv, 'b',linewidth=1.5, label='Sur RV')
    axes_c[0].plot(prescription.universe, via_l_appli, 'g', linewidth=1.5,label='Via l\'Appli')
    axes_c[0].set_title('Prescription Ordonnance')
    axes_c[0].legend()

    axes_c[1].plot(laborantin.universe, bilan, 'b', linewidth=1.5,label='Faire un bilan')
    axes_c[1].plot(laborantin.universe, test, 'g', linewidth=1.5,label='Faire un test')
    axes_c[1].plot(laborantin.universe, scan, 'r', linewidth=1.5,label='Faire un scan')
    axes_c[1].set_title('Voir un laborantin')
    axes_c[1].legend()
    
    y_clic_grippe_faible = fuzz.interp_membership(grippe.universe, toux_faible, x)
    y_clic_grippe_rhume = fuzz.interp_membership(grippe.universe, rhume, x)
    y_clic_grippe_fort = fuzz.interp_membership(grippe.universe, toux_fort, x)

    y_clic_palu_fort = fuzz.interp_membership(palu.universe, dm_fort, y)
    y_clic_palu_moyenne = fuzz.interp_membership(palu.universe, dm_moyenne, y)
    y_clic_palu_leger = fuzz.interp_membership(palu.universe, dm_leger, y)

    y_clic_omicron_pt = fuzz.interp_membership(omicron.universe, pt_appetit, z)
    y_clic_omicron_pm = fuzz.interp_membership(omicron.universe, pm_appetit, z)
    y_clic_omicron_sp = fuzz.interp_membership(omicron.universe, sp_appetit, z)

    y_clic_prescription_sur_rv_toux = fuzz.interp_membership(prescription.universe, sur_rv, x)
    y_clic_prescription_via_app_toux = fuzz.interp_membership(prescription.universe, via_l_appli, x)

    y_clic_prescription_sur_rv_palu = fuzz.interp_membership(prescription.universe, sur_rv, y)
    y_clic_prescription_via_app_palu = fuzz.interp_membership(prescription.universe, via_l_appli, y)

    y_clic_prescription_sur_rv_omicron = fuzz.interp_membership(prescription.universe, sur_rv, z)
    y_clic_prescription_via_app_omicron = fuzz.interp_membership(prescription.universe, via_l_appli, z)

    bilan_palu = fuzz.interp_membership(laborantin.universe, bilan, x)
    test_palu = fuzz.interp_membership(laborantin.universe, test, x)
    scan_palu = fuzz.interp_membership(laborantin.universe, scan, x)

    bilan_toux = fuzz.interp_membership(laborantin.universe, bilan, y)
    test_toux = fuzz.interp_membership(laborantin.universe, test, y)
    scan_toux = fuzz.interp_membership(laborantin.universe, scan, y)

    bilan_om = fuzz.interp_membership(laborantin.universe, bilan, z)
    test_om = fuzz.interp_membership(laborantin.universe, test, z)
    scan_om = fuzz.interp_membership(laborantin.universe, scan, z)

    graph=get_graph()
    return graph ,round(scan_om*100),round(test_om*100),round(bilan_om*100),round(scan_toux*100),round(test_toux*100),round(bilan_toux*100),round(scan_palu*100),round(test_palu*100),round(bilan_palu*100),round(y_clic_prescription_via_app_omicron*100),round(y_clic_prescription_sur_rv_omicron*100),round(y_clic_prescription_via_app_palu*100),round(y_clic_prescription_sur_rv_palu*100),round(y_clic_prescription_via_app_toux*100),round(y_clic_prescription_sur_rv_toux*100), round(y_clic_grippe_faible*100) ,round(y_clic_grippe_rhume*100),round(y_clic_grippe_fort*100),round(y_clic_palu_fort*100),round(y_clic_palu_moyenne*100),round(y_clic_palu_leger*100),round(y_clic_omicron_pt*100),round(y_clic_omicron_pm*100),round(y_clic_omicron_sp*100)

