from django.urls import path

from main.views import show_main, show_experience, create_experience, show_projects, create_project, get_projects_json, \
    delete_project, get_experience_json, delete_experience, register, login_user, logout_user, toggle_star_project, \
    toggle_star_experience, edit_experience, edit_project, create_project_ajax

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/edit/<uuid:experience_id>/", edit_experience, name="edit_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("projects/edit/<uuid:project_id>/", edit_project, name="edit_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/<uuid:project_id>/star/", toggle_star_project, name="toggle_star_project"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]