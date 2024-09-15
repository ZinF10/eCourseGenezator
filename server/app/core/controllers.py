from core import login_manager, dao

@login_manager.user_loader
def load_user(user_id):
    return dao.fetch_user(id=user_id)
