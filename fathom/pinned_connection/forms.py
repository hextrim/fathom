# pinned_connection : forms
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, FloatField, BooleanField, SubmitField#, Form
from wtforms.validators import DataRequired, NumberRange

class PinConnection(FlaskForm):
    F_ED = FloatField('F_ED', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    d_0 = FloatField('d_0', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    d = FloatField('d', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    t_in = FloatField('t_in', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    t_out = FloatField('t_out', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    g = FloatField('g', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    gamma_M0 = FloatField('gamma_M0', validators=[DataRequired(), NumberRange(min=1, message=("Value must be equal or greater than 1."))])
    gamma_M2 = FloatField('gamma_M2', validators=[DataRequired(), NumberRange(min=1, message=("Value must be equal or greater than 1."))])
    gamma_M6 = FloatField('gamma_M6', validators=[DataRequired(), NumberRange(min=1, message=("Value must be greater than 1."))])
    gamma_M6_ser = FloatField('gamma_M6_ser', validators=[DataRequired(), NumberRange(min=1, message=("Value must be equal or greater than 1."))])
    SF = FloatField('SF', validators=[DataRequired(), NumberRange(min=1, message=("Value must be equal or greater than 1."))])
    f_y = FloatField('f_y', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    f_yp = FloatField('f_yp', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    f_up = FloatField('f_up', validators=[DataRequired(), NumberRange(min=0.0001, message=("Value must be greater than 0."))])
    E = FloatField('E', validators=[DataRequired(), NumberRange(min=0.0001, message="Value must be greater than 0.")])
    unit_l = SelectField('unit_l', choices=[('m', 'm'), ('dm', 'dm'), ('cm', 'cm'), ('mm', 'mm')], validate_choice=True)
    unit_f = SelectField('unit_f', choices=[('N', 'N'), ('daN', 'daN'), ('hN', 'hN'), ('kN', 'kN'), ('MN', 'MN')], validate_choice=True)
    unit_s = SelectField('unit_s', choices=[('Pa', 'Pa'), ('daPa', 'daPa'), ('hPa', 'hPa'), ('kPa', 'kPa'), ('MPa', 'MPa')], validate_choice=True)
    isReplaceable = BooleanField('isReplaceable', default=False, false_values=('no', 'False'))
    submit = SubmitField('Calculate')
