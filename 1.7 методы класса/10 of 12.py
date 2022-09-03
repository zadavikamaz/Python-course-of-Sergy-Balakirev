class AppStore:
    applications = []

    def add_application(self, app):
        self.applications.append(app)

    def remove_application(self, app):
        self.applications.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.applications)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)