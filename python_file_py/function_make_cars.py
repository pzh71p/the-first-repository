def make_cars(manufacturer, model, tow_package=True, **more_about):
    more_about['manufacturer'] = manufacturer
    more_about['model'] = model
    more_about['tow_package'] = tow_package
    return more_about

