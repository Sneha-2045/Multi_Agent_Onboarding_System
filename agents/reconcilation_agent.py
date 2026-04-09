
def reconcile(old, new):

    updated = old.copy()

    for key, value in new.items():

        if value:
            updated[key] = value

    return updated