from rest_framework import permissions
# from rest_framework.permissions import BasePermission
#
#
# class IsAuthor(BasePermission):
#
#     # работа с одним объектом (для update, delete, details)
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and obj.author == request.user

    # def has_permission(self, request, view):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     return bool(request.user and request.user.is_staff)