from zillow import Zillow
from google_form import GoogleForm

zillow_obj = Zillow()
apartments = zillow_obj.get_apartments()
len_apartments = zillow_obj.get_len()

google_form_obj = GoogleForm()
google_form_obj.save_all(apartments, len_apartments)

print("All Done!")
