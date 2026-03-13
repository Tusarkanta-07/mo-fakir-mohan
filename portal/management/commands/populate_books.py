"""
Management command to populate books from the books directory
"""
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from portal.models import Book


class Command(BaseCommand):
    help = 'Populate books from the books directory into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting book population...')
        
        books_dir = settings.BOOKS_DIR
        
        if not os.path.exists(books_dir):
            self.stderr.write(f'Books directory not found: {books_dir}')
            return
        
        # Book title mappings (filename to Odia and English titles)
        book_titles = {
            'Chha Mana Atha Guntha by Fakir Mohan Senapati (Odia).pdf': {
                'odia': 'ଛମାଣ ଆଠଗୁଣ୍ଠ',
                'english': 'Chha Mana Atha Guntha (Six Acres and Two Cents)',
                'description_odia': 'ଓଡ଼ିଆ ସାହିତ୍ୟର ପ୍ରଥମ ଉପନ୍ୟାସ',
                'description_en': 'The first novel in Odia literature, a satire on colonial society',
            },
            'Rebati FM.pdf': {
                'odia': 'ରେବତୀ',
                'english': 'Rebati',
                'description_odia': 'ଫକୀର ମୋହନଙ୍କ ପ୍ରସିଦ୍ଧ କ୍ଷୁଦ୍ର ଗଳ୍ପ',
                'description_en': "A tragic short story about a young girl's quest for education",
            },
            'Patent medicine FM.pdf': {
                'odia': 'ପେଟେଣ୍ଟ ମେଡିସିନ୍',
                'english': 'Patent Medicine',
                'description_odia': 'ଏକ ବ୍ୟଙ୍ଗାତ୍ମକ ଗଳ୍ପ',
                'description_en': 'A satirical story on quack medicine and superstition',
            },
            'Mamu FM.pdf': {
                'odia': 'ମାମୁଁ',
                'english': 'Mamu (The Uncle)',
                'description_odia': 'ଫକୀର ମୋହନଙ୍କ କ୍ଷୁଦ୍ର ଗଳ୍ପ',
                'description_en': 'A short story about family relationships',
            },
            'Garudi mantra FM.pdf': {
                'odia': 'ଗାରୁଡ଼ ମନ୍ତ୍ର',
                'english': 'Garudi Mantra',
                'description_odia': 'ଅନ୍ଧବିଶ୍ୱାସ ଉପରେ ବ୍ୟଙ୍ଗ',
                'description_en': 'A story satirizing superstition and blind faith',
            },
            'Dakamunis FMU.pdf': {
                'odia': 'ଡାକମୁନିସ',
                'english': 'Dakamunis',
                'description_odia': 'ଫକୀର ମୋହନଙ୍କ ରଚନା',
                'description_en': 'A work by Fakir Mohan Senapati',
            },
            'Birei bisala FM.pdf': {
                'odia': 'ବିରେଇ ବିସାଳ',
                'english': 'Birei Bisala',
                'description_odia': 'ଫକୀର ମୋହନଙ୍କ ରଚନା',
                'description_en': 'A work by Fakir Mohan Senapati',
            },
            'RP Ananta FM.pdf': {
                'odia': 'ଆତ୍ମଜୀବନୀ',
                'english': 'Atmajibani (Autobiography)',
                'description_odia': 'ଫକୀର ମୋହନ ସେନାପତିଙ୍କ ଆତ୍ମଜୀବନୀ',
                'description_en': 'The autobiography of Fakir Mohan Senapati',
            },
        }
        
        created_count = 0
        updated_count = 0
        
        for filename in os.listdir(books_dir):
            if filename.endswith('.pdf'):
                file_path = os.path.join(books_dir, filename)
                file_size = os.path.getsize(file_path)
                
                # Format file size
                size_kb = file_size / 1024
                if size_kb > 1024:
                    size_str = f'{size_kb/1024:.1f} MB'
                else:
                    size_str = f'{size_kb:.1f} KB'
                
                # Get title info
                titles = book_titles.get(filename, {})
                title_odia = titles.get('odia', filename.replace('.pdf', ''))
                title_en = titles.get('english', '')
                desc_odia = titles.get('description_odia', '')
                desc_en = titles.get('description_en', '')
                
                # Check if book already exists
                book, created = Book.objects.get_or_create(
                    file_path=filename,
                    defaults={
                        'title_odia': title_odia,
                        'title_en': title_en,
                        'description_odia': desc_odia,
                        'description_en': desc_en,
                        'file_size': size_str,
                        'is_active': True,
                    }
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(f'  Created: {title_odia}')
                else:
                    updated_count += 1
                    # Update existing book
                    book.title_odia = title_odia
                    book.title_en = title_en
                    book.description_odia = desc_odia
                    book.description_en = desc_en
                    book.file_size = size_str
                    book.save()
                    self.stdout.write(f'  Updated: {title_odia}')
        
        self.stdout.write(self.style.SUCCESS(
            f'\nSuccessfully populated books! Created: {created_count}, Updated: {updated_count}'
        ))
