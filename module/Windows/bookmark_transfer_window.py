from module.UI.bookmark_transfer import BookmarkTransferApp


def __init__(self):
    super().__init__()
    self.ui = BookmarkTransferApp()
    self.ui.init_ui(self)
