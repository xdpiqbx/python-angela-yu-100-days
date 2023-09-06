from extensions import login_manager

# @login_manager.user_loader
# def user_loader(email):
#     if email not in users:
#         return
#
#     user = CurrentUser()
#     user.id = email
#     return user
#
#
# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return
#
#     user = CurrentUser()
#     user.id = email
#     return user
