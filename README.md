# clone-Udemy

Для того чтобы заработала библиотека languages нужно добавить в venv/lib/languages/fields.py строку: self.db_collation = False
И в venv/lib/languages/languages.py заменить импорт ugettext_lazy на gettext_lazy 
