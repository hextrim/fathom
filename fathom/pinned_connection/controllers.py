# pinned_connection : controllers

from distutils.util import strtobool
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_security import auth_required, roles_accepted
from .forms import PinConnection
from .PinnedConnectionClass import *
import math

pinned_connection_blueprint = Blueprint('pinned_connection_blueprint', __name__, static_url_path='', static_folder='../templates/dist', template_folder='../template/dist')


@pinned_connection_blueprint.route('/pinned-connection', methods=['GET', 'POST'])
@auth_required()
@roles_accepted('admins', 'moderators', 'users')
def pinned_connection_blueprint_view():
    form = PinConnection(request.form)
    print(form.errors)
    output_geometry = {}
    utilization = {}
    if request.method == 'GET':
        return render_template('pinned_connection.html', form=form, output_geometry=output_geometry, utilization=utilization)
    if request.method == 'POST':
        #F_ED = request.form['F_ED']
        #d_0 = request.form['d_0']
        #d = request.form['d']
        #t_in = request.form['t_in']
        #t_out = request.form['t_out']
        #g = request.form['g']
        #gamma_M0 = request.form['gamma_M0']
        #gamma_M2 = request.form['gamma_M2']
        #gamma_M6 = request.form['gamma_M6']
        #gamma_M6_ser = request.form['gamma_M6_ser']
        #f_y = request.form['f_y']
        #f_yp = request.form['f_yp']
        #f_up = request.form['f_up']
        #E = request.form['E']
        #unit_l = request.form['unit_l']
        #unit_f = request.form['unit_f']
        #unit_s = request.form['unit_s']
        isReplaceablePin = request.form['isReplaceable']
        ##############################################
        F_ED = form.F_ED.data
        d_0 = form.d_0.data
        d = form.d.data
        t_in = form.t_in.data
        t_out = form.t_out.data
        g = form.g.data
        gamma_M0 = form.gamma_M0.data
        gamma_M2 = form.gamma_M2.data
        gamma_M6 = form.gamma_M6.data
        gamma_M6_ser = form.gamma_M6_ser.data
        SF = form.SF.data
        f_y = form.f_y.data
        f_yp = form.f_yp.data
        f_up = form.f_up.data
        E = form.E.data
        unit_l = form.unit_l.data
        unit_f = form.unit_f.data
        unit_s = form.unit_s.data
        isReplaceable = form.isReplaceable.data
        isrep = form.isReplaceable
        print(F_ED)
        print(d_0)
        print(d)
        print(t_in)
        print(t_out)
        print(g)
        print(gamma_M0)
        print(gamma_M2)
        print(gamma_M6)
        print(gamma_M6_ser)
        print(f_y)
        print(f_yp)
        print(f_up)
        print(E)
        print(unit_l)
        print(unit_f)
        print(unit_s)
        print("pin: " + str(isReplaceable))
        print("pin: " + str(isReplaceablePin))
        print(isrep)

 #   if request.method == 'POST' and form.validate_on_submit():
 #       flash('Form submitted for calculation !','success')
 #       print('dupa')
 #   elif request.method == 'POST' and not form.validate_on_submit():
 #       flash('Please fill all fields before sending a request !','danger')
 #   else:
 #       return render_template('pinned_connections.html', form=form)
    if request.method == 'POST' and form.validate_on_submit():
        F_ED = form.F_ED.data
        d_0 = form.d_0.data
        d = form.d.data
        t_in = form.t_in.data
        t_out = form.t_out.data
        g = form.g.data
        gamma_M0 = form.gamma_M0.data
        gamma_M2 = form.gamma_M2.data
        gamma_M6 = form.gamma_M6.data
        gamma_M6_ser = form.gamma_M6_ser.data
        SF = form.SF.data
        f_y = form.f_y.data
        f_yp = form.f_yp.data
        f_up = form.f_up.data
        E = form.E.data
        unit_l = form.unit_l.data
        unit_f = form.unit_f.data
        unit_s = form.unit_s.data
        isReplaceable = form.isReplaceable.data
        isrep = form.isReplaceable
        print(F_ED)
        print(d_0)
        print(d)
        print(t_in)
        print(t_out)
        print(g)
        print(gamma_M0)
        print(gamma_M2)
        print(gamma_M6)
        print(gamma_M6_ser)
        print(f_y)
        print(f_yp)
        print(f_up)
        print(E)
        print(unit_l)
        print(unit_f)
        print(unit_s)
        print("pin: " + str(isReplaceable))
        print("pin: " + str(isReplaceablePin))
        print(isrep)
        ###############
        isPinReplaceable = isReplaceable
        inputs_geometry_A = {
            'inner_plate_thickness' : t_in,
            'outer_plate_thickness': t_out,
            'gap': g,
            'pin_diameter': d,
            'pin_hole': d_0
        }
        loads = {
            'Fv_Ed': F_ED
        }
        safety_factors = {
            'SF': SF,
            'gamma_M0': gamma_M0,
            'gamma_M2': gamma_M2,
            'gamma_M6': gamma_M6,
            'gamma_M6_ser': gamma_M6_ser
        }
        material_properties = {
            'pin_ultimate_tensile_strength': f_up,
            'pin_yield_strength': f_y,
            'plate_yield_strength': f_yp,
            'elastic_modulus': E
        }
        unit_system = {
            'units_force': unit_f,
            'units_stress': unit_s,
            'units_length': unit_l      
        }

        pinnedConnection_A = PinnedConnection_A_given_thickness(isPinReplaceable, inputs_geometry_A, unit_system, loads, safety_factors, material_properties)

        output_geometry = {
            'a': pinnedConnection_A.get_min_a(),
            'c': pinnedConnection_A.get_min_c()
        }

        utilization = {
            'Fv_Ed': pinnedConnection_A.Fv_Ed,
            'Fv_Rd': pinnedConnection_A.get_pin_shear_resistance(),
            'Fv_Util': pinnedConnection_A.get_pin_shear_utilization(),
            
            'sigma_h_Ed': pinnedConnection_A.get_contact_bearing_stress(),
            'fh_Ed':  pinnedConnection_A.get_contact_bearing_stress_resistance(),
            'sigma_h_Util': pinnedConnection_A.get_contact_bearing_stress_utilization(),
            
            'Fb_Ed': pinnedConnection_A.Fv_Ed,
            'Fb_Rd': pinnedConnection_A.get_plate_and_pin_bearing_resistance(),
            'Fb_Util': pinnedConnection_A.get_plate_and_pin_bearing_utilization(),
            
            'M_Ed': pinnedConnection_A.get_pin_bending_moment(),
            'M_Rd': pinnedConnection_A.get_pin_bending_resistance(),
            'M_Util': pinnedConnection_A.get_pin_bending_utilization(),

            'Fv_Ed_M_Ed_Util': pinnedConnection_A.get_combined_shear_and_bending_utilization()
        }

        print(output_geometry)
        print(utilization)
        flash('Form submitted for calculation !','success')
        #return redirect(url_for('pinned.pinned_view', form=form, output_geometry=output_geometry, utilization=utilization))
        return render_template('pinned_connection.html', form=form, output_geometry=output_geometry, utilization=utilization)
    elif request.method == 'POST' and not form.validate_on_submit():
        flash('Please fill all fields correctly before submitting a form!','danger')
        return render_template('pinned_connection.html', form=form, output_geometry=output_geometry, utilization=utilization)
    else:
        flash('Invalid request submitted!','danger')
        return redirect(request.url)
        #return render_template('pinned_connection.html', form=form, output_geometry=output_geometry, utilization=utilization)

