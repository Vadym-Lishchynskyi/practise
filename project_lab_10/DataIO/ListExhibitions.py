from project.Instances import Exhibition_category_inst, Exhibition_inst

all_exhibitions = []
all_categories = []


def new_exhibition(ex):
    # if isinstance(ex, Exhibition_inst):
    all_exhibitions.append(ex)


def new_category(cat):
    # if isinstance(cat, Exhibition_category_inst):
    all_categories.append(cat)
