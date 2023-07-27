import os
from ukrainian_armor_manager import UkrainianArmorManager
from notification_manager import NotificationManager

# base_url = "https://ukrainianarmor.com/product/"
# color = "attribute_pa_color=multicam"
#
# urls = [
#     f"{base_url}plytonoska-fpc-bez-plyt/?{color}&attribute_pa_size=l",
#     f"{base_url}kamerband-csa-dlya-rpc/?attribute_pa_size=l",
#     f"{base_url}zahyst-klyuchyczi-cam/?{color}",
#     f"{base_url}zahyst-pahu-gam/?{color}",
#     f"{base_url}bronovanyj-rozvantazhuvalnyj-poyas-awb/?{color}&attribute_pa_size=s-m"
# ]

armor = UkrainianArmorManager()
armor.request_raw_data_from_urls()
armor.save_scraped_data_to_json()

message = armor.prepared_message_with_dropped_prices()

if message:
    notification = NotificationManager()
    notification.send_email(message, [os.environ["SECONDARY_MAIL"]])
    print("Mail was send")

