test_settings= {
    "Theme":"dark",
    "Language" : "english",
    "Notifications" : "enabled"    
}
more_setting= ("Volume", "high")

def add_setting(settings_dict,key_value_tuple):
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower()
    
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict,key_value_tuple):
    key,value = key_value_tuple
    key_lower = key.lower()
    value_lower = value.lower()
    if key_lower in settings_dict:
        settings_dict[key_lower] = value_lower 
        return f"Setting '{key_lower}' updated to '{value_lower}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
        

def delete_setting(settings_dict,key):

    low_key = key.lower()
    if low_key in settings_dict :
        del settings_dict[low_key]
        return f"Setting '{low_key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings_dict.items():
        capitalized_key = key.capitalize()
        result += f"{capitalized_key}: {value}\n"
    return result
