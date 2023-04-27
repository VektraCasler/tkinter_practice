# abq_data_entry/widgets.py


# CLASSES ------------------------------------------------

class ValidatedMixin:
    """Adds a validation functionality to an input widget"""

    def __init__(self, *args, error_var=None, **kwargs):
        self.error = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)
        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)
        self.configure(
            validate='all',
            validatecommand=(vcmd, '%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(invcmd, '%P', '%s', '%S', '%V', '%i', '%d')
        )

    def _toggle_error(self, on=False):
        self.configure(foreground=('red' if on else 'black'))

    def _validate(self, proposed, current, char, event, index, action):
        """The validation method.  Don't override this, override _key_validate, and _focus_validate."""
        self.error.set('')
        self._toggle_error()
        valid = True
        # if the widget is disabled, don't validate
        state = str(self.configure('state')[-1])
        if state == tk.DISABLED:
            return valid
        if event == 'focusout':
            valid = self._focusout_validate(event=event)
        elif event == 'key':
            valid = self._key_validate(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )
        return valid

    def _focusout_validate(self, **kwargs):
        return True

    def _key_validate(self, **kwargs):
        return True

    def _invalid(self, proposed, current, char, event, index, action):
        if event == 'focusout':
            self._focusout_invalid(event=event)
        elif event == 'key':
            self._key_invalid(
                proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action
            )

    def _focusout_invalid(self, **kwargs):
        """Handle invalid data on a focus event."""
        self._toggle_error(True)

    def _key_invalid(self, **kwargs):
        """Handle invalid data on a key event.  By default we want to do nothing."""
        pass

    def trigger_focusout_validation(self):
        valid = self._validate('', '', '', 'focusout', '', '')
        if not valid:
            self._focusout_invalid(event='focusout')
        return valid


class DateEntry(ValidatedMixin, ttk.Entry):
    """An Entry that only accepts ISO Date strings"""

    def _key_validate(self, action, index, char, **kwargs):
        valid = True
        if action == '0':  # This is a delete action
            valid = True
        elif index in ('0', '1', '2', '3', '5', '6', '8', '9'):
            valid = char.isdigit()
        elif index in ('4', '7'):
            valid = char == '-'
        else:
            valid = False
        return valid

    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            self.error.set('A value is required')
            valid = False
        try:
            datetime.strptime(self.get(), '%Y-%m-%d')
        except ValueError:
            self.error.set('Invalid date')
            valid = False
        return valid


class RequiredEntry(ValidatedMixin, ttk.Entry):
    """An Entry that requires a value"""

    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid


class ValidatedCombobox(ValidatedMixin, ttk.Combobox):
    """A combobox that only takes values from its string list"""

    def _key_validate(self, proposed, action, **kwargs):
        valid = True
        # if the user tries to delete,
        # just clear the field
        if action == '0':
            self.set('')
            return True

        # get our values list
        values = self.cget('values')
        # Do a case-insensitive match against the entered text
        matching = [
        x for x in values
        if x.lower().startswith(proposed.lower())
        ]
        if len(matching) == 0:
            valid = False
        elif len(matching) == 1:
            self.set(matching[0])
            self.icursor(tk.END)
            valid = False
        return valid

    def _focusout_validate(self, **kwargs):
        valid = True
        if not self.get():
            valid = False
            self.error.set('A value is required')
        return valid


