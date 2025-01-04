# import os
#
# from dotenv import load_dotenv
#
# load_dotenv()
#
#
# class ModelBaseFactory:
#
#     @staticmethod
#     def get_used_db_type():
#
#         db_type = os.getenv("DATABASE")
#
#         if db_type == "MONGODB":
#
#             return True
#
#     @staticmethod
#     def get_chat_repository():
#         pass