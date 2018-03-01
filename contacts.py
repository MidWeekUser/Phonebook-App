import os

class Contacts(object):

    def __init__(self, cachedir):
        self.entries = {}
        self.cachedir = str(cachedir)
        self.filename = 'contacts.txt'

        if not os.path.exists(self.cachedir):
            os.mkdir(self.cachedir)
        self.file_cache = open(os.path.join(self.cachedir, self.filename), 'w')

    def add_contact(self, name, phonenumber):
        self.entries[name] = phonenumber

    def remove_contact(self, name, phonenumber):
    	del self.entries[name]

    def check_name(self, name):
        return self.entries[name]

    def get_all_names(self):
        return self.entries.keys()

    def get_phone_numbers(self):
        return self.entries.values()

    def consistency(self):
        phone_numbers = list(self.get_phone_numbers())

        for i in range(len(phone_numbers) - 1):
            for j in range(i + 1, len(phone_numbers)):
                if phone_numbers[j].startswith(phone_numbers[i]) or\
                   phone_numbers[i].startswith(phone_numbers[j]):
                    return False
        return True

    def clear(self):
        self.entries = {}
        self.file_cache.close()
        os.remove(os.path.join(self.cachedir, self.filename))
        os.rmdir(self.cachedir)