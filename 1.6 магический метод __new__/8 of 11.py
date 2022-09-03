TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    __name = None
    __obj = None

    def __new__(cls, *args, **kwargs):
        cls.__name = args[0]
        if TYPE_OS == 1:
            cls.__obj = super().__new__(DialogWindows)
            cls.__obj.name = cls.__name
        else:
            cls.__obj = super().__new__(DialogLinux)
            cls.__obj.name = cls.__name
        return cls.__obj

# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         obj = DialogWindows() if TYPE_OS == 1 else DialogLinux()
#         setattr(obj, 'name', args[0])
#         return obj


dlg = Dialog('12345')
print(dlg.name)