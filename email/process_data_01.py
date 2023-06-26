def process_data(data_dict):
    process_data = {}
    process_data["name"] = data_dict["nickname"]
    process_data["email"] = data_dict["email"]
    process_data["fortune"] = int(data_dict["fortune_id"])
    process_data["goals"] = data_dict["goals"]
    return process_data
