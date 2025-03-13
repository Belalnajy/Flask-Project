from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FloatField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length,EqualTo, Optional,URL

class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    publish_date = DateField('Publish Date', validators=[DataRequired()])
    add_to_site_at = DateField('Add to Site At', validators=[DataRequired()])
    author_id = SelectField('Author', choices=[], coerce=int) 
    image_url = StringField("Image URL", validators=[Optional(), URL()])
    description = TextAreaField("Description", validators=[Optional()])
    price = FloatField('Price', validators=[DataRequired()])
    appropriate = SelectField(
        'Appropriate for',
        choices=[('under 8', 'Under 8'), ('8-15', '8-15'), ('adults', 'Adults')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Add Book')

class AuthorForm(FlaskForm):
    name = StringField('Author Name', validators=[DataRequired()])
    submit = SubmitField('Add Author')

