# Config class model
class OrganisationUnitConfig:
    def __init__(self, has_fixed_memebership_fee, fixed_memebership_amount):
        self.has_fixed_memebership_fee = has_fixed_memebership_fee
        self.fixed_memebership_amount = fixed_memebership_amount

# Organisation unit class model
class OrganisationUnit:
    def __init__(self, name, config=None, parent=None):
        self.name = name
        self.children = []

        # If parent, connect parent with add_child function
        if parent:
            parent.add_child(self)
        else:
            self.parent = parent

        # If config, create config class instance
        if config:
            self.config = OrganisationUnitConfig(config[0], config[1])
        else:
            self.config = config

    # Add child to config unit and pair child with parent
    def add_child(self, child):
        self.children.append(child)
        child.parent = self