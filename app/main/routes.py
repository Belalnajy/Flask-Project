from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Book, Author
from app.main.forms import BookForm, AuthorForm
from app import db
from flask_login import login_required
from utils.decorators import admin_required

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def book_page():
    books = Book.query.all()
    return render_template('pages/index.html', books=books)

@main.route('/book_details/<int:book_id>')
@login_required
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('pages/book_details.html', book=book)

@main.route('/book_form', methods=['GET', 'POST'])
@admin_required
def book_form():
    form = BookForm()
    form.author_id.choices = [(author.id, author.name) for author in Author.query.all()]
    if form.validate_on_submit():
        new_book = Book(
            name=form.name.data,
            publish_date=form.publish_date.data,
            add_to_site_at=form.add_to_site_at.data,
            author_id=form.author_id.data,
            price=form.price.data,
            appropriate=form.appropriate.data,
            description=form.description.data,
            image_url=form.image_url.data
        )
        new_book.save_to_db()
        flash("Book added successfully!", "success")
        return redirect(url_for("main.book_page"))

    return render_template("pages/book_form.html", form=form)

@main.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
@admin_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id) 
    form = BookForm(obj=book)

    form.author_id.choices = [(author.id, author.name) for author in Author.query.all()]

    if form.validate_on_submit():
        book.name = form.name.data
        book.publish_date = form.publish_date.data
        book.add_to_site_at = form.add_to_site_at.data
        book.author_id = form.author_id.data
        book.price = form.price.data
        book.appropriate = form.appropriate.data
        book.description = form.description.data
        book.image_url = form.image_url.data

        db.session.commit() 
        flash('Book updated successfully!', 'success')
        return redirect(url_for('main.book_page'))

    return render_template('pages/book_form.html', form=form, is_edit=True)


@main.route('/delete_book/<int:book_id>', methods=['POST'])
@admin_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('main.book_page'))

@main.route('/author_form', methods=['GET', 'POST'])
@admin_required
def author_form():
    form = AuthorForm()
    author = Author.query.all()
    if form.validate_on_submit():
        new_author = Author(name=form.name.data)
        db.session.add(new_author)
        db.session.commit()
        flash('Author added successfully!', 'success')
        return redirect(url_for('main.author_form'))

    return render_template('pages/author_form.html', form=form, author=author)

@main.route('/author_details/<int:author_id>')
@admin_required
def author_details(author_id):
    books = Book.query.filter_by(author_id=author_id).all()
    author = Author.query.get_or_404(author_id)
    return render_template('pages/author_details.html', author=author, books=books)

@main.route('/delete_author/<int:author_id>', methods=['POST'])
@admin_required
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    flash('Author deleted successfully!', 'success')
    return redirect(url_for('main.author_form'))

