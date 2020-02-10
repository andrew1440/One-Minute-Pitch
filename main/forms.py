from flask_wtf import FlaskForm
from wtforms import stringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators = [Required])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    pitch_title = StringField('Title', validators=[Required()])
    content = TextAreaField('Your Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Interview-Pitch','Interview Pitch'),('Product Pitch'),('Promotion Pitch','Business Pitch'], validators[Required()])
    submit = SubmitField('Comment')
    