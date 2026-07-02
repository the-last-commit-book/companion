# chapter_05_door_that_opened_twice.py
# The Last Commit: Learn Python by Solving a Murder Mystery
# Chapter 5: The Door That Opened Twice

victim = "Marcus Thorne"
door_name = "EAST_BALCONY_DOOR"

first_open_time = "00:08"
first_close_time = "00:09"
second_open_time = "00:15"

last_confirmed_location = "outside"
reentry_event_found = False
second_open_recorded_side = "inside"
second_open_recorded_user = "Marcus Thorne"

print("Door review:", door_name)
print("First opening:", first_open_time)
print("Door closed:", first_close_time)
print("Second opening:", second_open_time)
print()

if second_open_recorded_user == victim:
    print("The second opening is recorded under Marcus Thorne's identity.")

if last_confirmed_location == "outside":
    print("Marcus's last confirmed location before 00:15: outside the balcony door.")

if reentry_event_found == False:
    print("No re-entry event was found between 00:09 and 00:15.")

if second_open_recorded_side == "inside":
    print("The 00:15 opening is recorded as coming from inside the house.")

if last_confirmed_location == "outside" and reentry_event_found == False and second_open_recorded_side == "inside":
    print("Contradiction: Marcus could not open the east balcony door from inside at 00:15.")
