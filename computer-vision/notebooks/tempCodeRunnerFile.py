def choose_tracker_type(current_tracker=None):
    print("\nChoose tracker type:")
    print("1 - CSRT  | More accurate, slower")
    print("2 - KCF   | Faster, medium accuracy")
    print("3 - MOSSE | Very fast, lower accuracy")

    if current_tracker:
        print(f"Press ENTER to keep current tracker: {current_tracker}")
    else:
        print("Press ENTER for default CSRT")

    choice = input("Your choice: ").strip()

    if choice == "2":
        return "KCF"
    if choice == "3":
        return "MOSSE"
    if current_tracker and choice == "":
        return current_tracker
    return "CSRT"


def create_tracker(tracker_name):
    """Create OpenCV tracker. Requires opencv-contrib-python."""
    trackers = {
        "CSRT":  cv2.legacy.TrackerCSRT_create,
        "KCF":   cv2.legacy.TrackerKCF_create,
        "MOSSE": cv2.legacy.TrackerMOSSE_create,
    }
    name = tracker_name.upper()
    if name not in trackers:
        raise ValueError(f"Unsupported tracker type: {tracker_name}")
    return trackers[name]()
