from django.core.management.base import BaseCommand
from portal.models import TimelineEvent


class Command(BaseCommand):
    help = 'Populate timeline events for Fakir Mohan Senapati'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating timeline events...')

        # Clear existing events
        TimelineEvent.objects.all().delete()
        self.stdout.write('Cleared existing events')

        # Timeline events data
        events = [
            # ବାଲ୍ୟକାଳ, ସଂଘର୍ଷ ଓ ଶିକ୍ଷକତା (୧୮୪୩ - ୧୮୬୫)
            {
                'year': 1843,
                'title_odia': 'ଜନ୍ମ',
                'title_en': 'Birth',
                'description_odia': 'ବାଲେଶ୍ୱର ଜିଲ୍ଲାର ମଲ୍ଲିକାଶପୁରଠାରେ ଜନ୍ମଗ୍ରହଣ। ତାଙ୍କର ମୂଳ ନାମ ଥିଲା ବ୍ରଜମୋହନ। ପିଲାଦିନେ ରୋଗଗ୍ରସ୍ତ ହେବାରୁ ଫକୀର ବେଶ କରାଯାଇଥିଲା, ତେଣୁ ନାମ ଫକୀର ମୋହନ ହୋଇଗଲା।',
                'order': 1
            },
            {
                'year': 1844,
                'title_odia': 'ପିତୃ ମାତୃ ବିୟୋଗ',
                'title_en': 'Parents Death',
                'description_odia': 'ମାତ୍ର ଦେଢ଼ ବର୍ଷ ବୟସରେ ପିତା ଲକ୍ଷ୍ମଣ ଚରଣ ସେନାପତି ଏବଂ ପରେ ମାତା ତୁଳସୀ ଦେବୀଙ୍କ ପରଲୋକ। ଜେଜେମାଙ୍କ ଦ୍ୱାରା ଲାଳିତପାଳିତ।',
                'order': 2
            },
            {
                'year': 1856,
                'title_odia': 'ପ୍ରଥମ ବିବାହ',
                'title_en': 'First Marriage',
                'description_odia': '୧୩ ବର୍ଷ ବୟସରେ ଲୀଳାବତୀ ଦେବୀଙ୍କ ସହ ପ୍ରଥମ ବିବାହ।',
                'order': 3
            },
            {
                'year': 1858,
                'title_odia': 'କର୍ମଜୀବନ ଆରମ୍ଭ',
                'title_en': 'Career Begins',
                'description_odia': 'ଆର୍ଥିକ ଅନାଟନ ଯୋଗୁଁ ସ୍କୁଲ ଛାଡ଼ିଲେ ଏବଂ ବାଲେଶ୍ୱର ବନ୍ଦରରେ ନିମକ ମାହାଲର ମୁନ୍‌ସୀ ଭାବେ କର୍ମଜୀବନ ଆରମ୍ଭ।',
                'order': 4
            },
            {
                'year': 1864,
                'title_odia': 'ପ୍ରଧାନ ଶିକ୍ଷକ',
                'title_en': 'Head Teacher',
                'description_odia': 'ବାଲେଶ୍ୱର ବାରବାଟୀ ସ୍କୁଲରେ ପ୍ରଧାନ ଶିକ୍ଷକ ଭାବେ ନିଯୁକ୍ତି। ଏହି ସମୟରେ ନିଜ ଉଦ୍ୟମରେ ବଙ୍ଗଳା, ସଂସ୍କୃତ ଓ ଇଂରାଜୀ ଭାଷା ଶିକ୍ଷା କରିଥିଲେ।',
                'order': 5
            },
            # ଭାଷା ଆନ୍ଦୋଳନ ଓ ପତ୍ରିକା ସମ୍ପାଦନା (୧୮୬୬ - ୧୮୭୦)
            {
                'year': 1866,
                'title_odia': 'ନଅଙ୍କ ଦୁର୍ଭିକ୍ଷ ଓ ବ୍ୟାକରଣ ରଚନା',
                'title_en': 'Famine Relief & Grammar',
                'description_odia': 'ନଅଙ୍କ ଦୁର୍ଭିକ୍ଷ ସମୟରେ ବାଲେଶ୍ୱରରେ ରିଲିଫ୍ ବଣ୍ଟନ କାର୍ଯ୍ୟର ତଦାରଖ। ସ୍କୁଲ ପିଲାଙ୍କ ପାଇଁ ସରଳ ଓଡ଼ିଆ ବ୍ୟାକରଣ ପୁସ୍ତକ ରଚନା।',
                'order': 6
            },
            {
                'year': 1867,
                'title_odia': 'ଉତ୍କଳ ଭାଷା ଉଦ୍ଦୀପନୀ ସଭା',
                'title_en': 'Utkal Bhasha Uddipani Sabha',
                'description_odia': 'ଓଡ଼ିଆ ଭାଷାର ପ୍ରସାର ପାଇଁ ବାଲେଶ୍ୱରରେ ଉତ୍କଳ ଭାଷା ଉଦ୍ଦୀପନୀ ସଭା ପ୍ରତିଷ୍ଠା।',
                'order': 7
            },
            {
                'year': 1868,
                'title_odia': 'ଉତ୍କଳ ପ୍ରିଣ୍ଟିଂ ପ୍ରେସ ଓ ପତ୍ରିକା',
                'title_en': 'Printing Press & Publications',
                'description_odia': 'ଓଡ଼ିଆ ଭାଷା ବିଲୋପ ଷଡ଼ଯନ୍ତ୍ରର କଡ଼ା ମୁକାବିଲା କରିବାକୁ ଯାଇ ବାଲେଶ୍ୱରରେ ଉତ୍କଳ ପ୍ରିଣ୍ଟିଂ ପ୍ରେସ ପ୍ରତିଷ୍ଠା। ଜୁଲାଇ ମାସରେ ବୋଧଦାୟିନୀ (ମାସିକ ପତ୍ରିକା) ଓ ବାଲେଶ୍ୱର ସମ୍ବାଦ ବାହିକା (ସମ୍ବାଦପତ୍ର) ପ୍ରକାଶନ ଆରମ୍ଭ।',
                'order': 8
            },
            {
                'year': 1869,
                'title_odia': 'ବ୍ରାହ୍ମସମାଜ ପ୍ରତିଷ୍ଠା',
                'title_en': 'Brahmo Samaj',
                'description_odia': 'ବାଲେଶ୍ୱରରେ ବ୍ରାହ୍ମସମାଜ ପ୍ରତିଷ୍ଠାରେ ସହାୟତା।',
                'order': 9
            },
            # ଗଡ଼ଜାତ ପ୍ରଶାସନ ଓ ରୋମାଞ୍ଚକର ଅଭିଜ୍ଞତା (୧୮୭୧ - ୧୮୯୬)
            {
                'year': 1871,
                'title_odia': 'ନୀଳଗିରି ଦେବାନ',
                'title_en': 'Nilgiri Dewan',
                'description_odia': 'ଜନ୍ ବିମ୍ସଙ୍କ ସୁପାରିଶରେ ନୀଳଗିରି ଗଡ଼ଜାତର ଦେବାନ ଭାବେ ଯୋଗଦାନ। ପ୍ରଥମ ପତ୍ନୀଙ୍କ ବିୟୋଗ ପରେ କୃଷ୍ଣା କୁମାରୀ ଦେଈଙ୍କ ସହ ଦ୍ୱିତୀୟ ବିବାହ।',
                'order': 10
            },
            {
                'year': 1887,
                'title_odia': 'ସ୍ୱଦେଶୀ କାରଖାନା',
                'title_en': 'Swadeshi Factory',
                'description_odia': 'ସ୍ୱଦେଶୀ କାରଖାନା ପ୍ରତିଷ୍ଠା କରିବାର ବିଫଳ ପ୍ରୟାସ।',
                'order': 11
            },
            {
                'year': 1891,
                'title_odia': 'ଭୂୟାଁ ମେଳି',
                'title_en': 'Bhuyan Meli (Peasant Revolt)',
                'description_odia': 'କେନ୍ଦୁଝରରେ ଦେବାନ ଥିବାବେଳେ ପ୍ରସିଦ୍ଧ ଭୂୟାଁ ମେଳି (କୃଷକ ବିଦ୍ରୋହ)। ଧରଣୀଧର ଭୂୟାଁଙ୍କ ଦ୍ୱାରା ବନ୍ଦୀ ହେବା ଏବଂ ପାନପତ୍ର ଡେମ୍ଫରେ ଗୁପ୍ତ ବାର୍ତ୍ତା ପଠାଇ ଇଂରେଜ ସୈନ୍ୟଙ୍କ ସାହାଯ୍ୟରେ ରକ୍ଷା ପାଇବା।',
                'order': 12
            },
            {
                'year': 1892,
                'title_odia': 'ଉତ୍କଳ ଭ୍ରମଣଂ',
                'title_en': 'Utkala Bhramanam',
                'description_odia': 'ବ୍ୟଙ୍ଗ କବିତା ଉତ୍କଳ ଭ୍ରମଣଂ ପ୍ରକାଶିତ।',
                'order': 13
            },
            {
                'year': 1894,
                'title_odia': 'ଦ୍ୱିତୀୟ ପତ୍ନୀଙ୍କ ବିୟୋଗ',
                'title_en': 'Second Wife Death',
                'description_odia': 'ଦ୍ୱିତୀୟ ପତ୍ନୀ କୃଷ୍ଣା କୁମାରୀଙ୍କ ଦେହାନ୍ତ। ସ୍ମୃତିରେ ପୁଷ୍ପମାଳା ରଚନା।',
                'order': 14
            },
            {
                'year': 1896,
                'title_odia': 'ଅବସର',
                'title_en': 'Retirement',
                'description_odia': 'ପ୍ରଶାସନିକ କାର୍ଯ୍ୟରୁ ଅବସର। କଟକରେ ବସବାସ ଓ ସମ୍ପୂର୍ଣ୍ଣ ସାହିତ୍ୟ ସାଧନା ଆରମ୍ଭ।',
                'order': 15
            },
            # ସାହିତ୍ୟିକ ମାଇଲଖୁଣ୍ଟ ଓ ଶେଷ ଜୀବନ (୧୮୯୭ - ୧୯୧୮)
            {
                'year': 1897,
                'title_odia': 'ଛମାଣ ଆଠ ଗୁଣ୍ଠ',
                'title_en': 'Chha Mana Atha Guntha',
                'description_odia': 'ଶ୍ରେଷ୍ଠ ଉପନ୍ୟାସ ଛମାଣ ଆଠ ଗୁଣ୍ଠ ଉତ୍କଳ ସାହିତ୍ୟ ପତ୍ରିକାରେ ଧୂର୍ଜଟି ଛଦ୍ମନାମରେ ଧାରାବାହିକ ପ୍ରକାଶନ ଆରମ୍ଭ (ପୁସ୍ତକ ରୂପେ ୧୯୦୨ ରେ ପ୍ରକାଶିତ)।',
                'order': 16
            },
            {
                'year': 1898,
                'title_odia': 'ରେବତୀ',
                'title_en': 'Revati',
                'description_odia': 'ଆଧୁନିକ ଓଡ଼ିଆ ସାହିତ୍ୟର ପ୍ରଥମ କ୍ଷୁଦ୍ରଗଳ୍ପ ରେବତୀ ପ୍ରକାଶିତ।',
                'order': 17
            },
            {
                'year': 1901,
                'title_odia': 'ଲଛମା',
                'title_en': 'Lachhama',
                'description_odia': 'ଐତିହାସିକ ଉପନ୍ୟାସ ଲଛମା ର ଧାରାବାହିକ ପ୍ରକାଶନ ଆରମ୍ଭ (ପୁସ୍ତକ- ୧୯୧୪)।',
                'order': 18
            },
            {
                'year': 1904,
                'title_odia': 'ଉତ୍କଳ ସାହିତ୍ୟ ସମାଜ',
                'title_en': 'Utkal Sahitya Samaja',
                'description_odia': 'ଉତ୍କଳ ସାହିତ୍ୟ ସମାଜର ସଭାପତି ଭାବେ ନିର୍ବାଚିତ।',
                'order': 19
            },
            {
                'year': 1906,
                'title_odia': 'ଶାନ୍ତିକାନନ',
                'title_en': 'Shantikana',
                'description_odia': 'ପତ୍ନୀଙ୍କ ସ୍ମୃତିରେ ବାଲେଶ୍ୱରରେ ବାସଭବନ ଶାନ୍ତିକାନନ ନିର୍ମାଣ।',
                'order': 20
            },
            {
                'year': 1909,
                'title_odia': 'ବୌଦ୍ଧାବତାର କାବ୍ୟ',
                'title_en': 'Bauddhabatara Kavya',
                'description_odia': 'ବୌଦ୍ଧାବତାର କାବ୍ୟ ପ୍ରକାଶିତ।',
                'order': 21
            },
            {
                'year': 1913,
                'title_odia': 'ମାମୁଁ',
                'title_en': 'Mamu',
                'description_odia': 'ସାମାଜିକ ଉପନ୍ୟାସ ମାମୁଁ ପ୍ରକାଶିତ।',
                'order': 22
            },
            {
                'year': 1914,
                'title_odia': 'ଉତ୍କଳ ସମ୍ମିଳନୀ ସଭାପତି',
                'title_en': 'Utkal Sammilani President',
                'description_odia': 'ପାରଳାଖେମୁଣ୍ଡିଠାରେ ଉତ୍କଳ ସମ୍ମିଳନୀର ଦଶମ ଅଧିବେଶନରେ ସଭାପତିତ୍ୱ।',
                'order': 23
            },
            {
                'year': 1915,
                'title_odia': 'ପ୍ରାୟଶ୍ଚିତ୍ତ ଓ ଆତ୍ମଜୀବନୀ',
                'title_en': 'Prayaschitta & Autobiography',
                'description_odia': 'ଶେଷ ଉପନ୍ୟାସ ପ୍ରାୟଶ୍ଚିତ୍ତ ପ୍ରକାଶିତ। ନିଜ ଆତ୍ମଜୀବନୀ ଲେଖିବା ଆରମ୍ଭ କଲେ।',
                'order': 24
            },
            {
                'year': 1917,
                'title_odia': 'ଗଳ୍ପ ସ୍ୱଳ୍ପ',
                'title_en': 'Galba Swalba',
                'description_odia': 'କ୍ଷୁଦ୍ରଗଳ୍ପ ସଂକଳନ ଗଳ୍ପ ସ୍ୱଳ୍ପ (ପ୍ରଥମ ଭାଗ) ପ୍ରକାଶିତ।',
                'order': 25
            },
            {
                'year': 1918,
                'title_odia': 'ପରଲୋକ',
                'title_en': 'Death',
                'description_odia': 'ବାଲେଶ୍ୱରର ଶାନ୍ତିକାନନଠାରେ ୭୫ ବର୍ଷ ବୟସରେ ପରଲୋକ।',
                'order': 26
            },
            # ମରଣୋତ୍ତର ପ୍ରକାଶନ (୧୯୨୦ - ୧୯୨୭)
            {
                'year': 1920,
                'title_odia': 'ଗଳ୍ପ ସ୍ୱଳ୍ପ (ଦ୍ୱିତୀୟ ଭାଗ)',
                'title_en': 'Galba Swalba Part 2',
                'description_odia': 'ଗଳ୍ପ ସ୍ୱଳ୍ପ ର ଦ୍ୱିତୀୟ ଭାଗ ପ୍ରକାଶିତ।',
                'order': 27
            },
            {
                'year': 1927,
                'title_odia': 'ଆତ୍ମଜୀବନ ଚରିତ',
                'title_en': 'Autobiography Published',
                'description_odia': 'ପୁତ୍ର ମୋହିନୀ ମୋହନଙ୍କ ଦ୍ୱାରା ତାଙ୍କର ସମ୍ପୂର୍ଣ୍ଣ ଆତ୍ମଜୀବନୀ ଆତ୍ମଜୀବନ ଚରିତ ପ୍ରକାଶିତ।',
                'order': 28
            },
        ]

        # Create events
        for event_data in events:
            event = TimelineEvent.objects.create(**event_data)
            self.stdout.write(f'  ✓ Created: {event.year} - {event.title_odia}')

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {len(events)} timeline events!'))
