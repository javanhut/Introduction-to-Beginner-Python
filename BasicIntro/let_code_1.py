# # Let's code a speech recognition program!
# import speech_recognition as sr
# import datetime
#
# microphone = sr.Microphone(device_index=2)
# recognizer = sr.Recognizer()
#
#
# # for index, name in enumerate(microphone.list_microphone_names()):
# #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
#
# class Assistant:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def print_user_text(user_text: str, enabled: bool = False) -> None | str:
#         if enabled:
#             return user_text
#         return None
#
#     def start_listening(self, enabled: bool = False) -> None:
#         with microphone as source:
#             print("Begin speaking now: ")
#             audio = recognizer.listen(source)
#         text_out = recognizer.recognize_google(audio)
#         if enabled:
#             print(self.print_user_text(user_text=text_out, enabled=enabled))
#         self.select_options(text_in=text_out)
#
#     @staticmethod
#     def select_options(text_in: str) -> None:
#         if "get" and "time" in text_in.lower():
#             date_time = datetime.timezone.utc
#             print(f"The time is {datetime.datetime.now()}")
#         if "your" and "name" in text_in.lower():
#             print("My name is Assistant. How can i help you?")
#         # add more options if you like!
#
#
# if "__main__" == __name__:
#     a1 = Assistant()
#     a1.start_listening(True)
