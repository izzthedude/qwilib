class Toggleable:
    def toggle_visibility(self):
        is_hidden = self.isHidden()
        self.setHidden(not is_hidden)


class Invisible:
    def set_invisible(self):
        self_size_policy = self.sizePolicy()
        self_size_policy.setRetainSizeWhenHidden(True)
        self.setSizePolicy(self_size_policy)
        self.setDisabled(True)
        self.setHidden(True)
