from django.urls import path
from rest_framework.routers import SimpleRouter

# from .views import PostList, PostDetail, UserList, UserDetail
from .views import PostViewSet, UserViewSet

# urlpatterns = [
#     path("", PostList.as_view(), name="post_list"),
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("users/", UserList.as_view(), name="user_list"),
#     path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
# ]

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")


urlpatterns = router.urls
