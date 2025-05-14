from tkinter import *

class TravelCompanionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Companion App")
        self.root.geometry("400x870")  # I increased the size to make everything fit neatly

        self.trip_list = []
        self.current_trip_index = 0
        self.error_message = StringVar()

        # Title and Clear All Checkboxes
        title_frame = Frame(self.root)
        title_frame.pack(pady=10, padx=10, fill="x")

        title_label = Label(title_frame, text="Travel Companion App", font=("Arial", 16, "bold"), bg="yellow", fg="blue")
        title_label.pack(side=LEFT, padx=5)

        # Clear all Checkboxes
        self.clear_all_var = BooleanVar()
        clear_all_checkbox = Checkbutton(title_frame, text="Clear All", font=("Arial", 10, "bold"), variable=self.clear_all_var, command=self.clear_all_if_checked, fg="red")
        clear_all_checkbox.pack(side=RIGHT, padx=5)

        # Trip Section
        create_trip_frame = LabelFrame(self.root, text="Create Trip", font=("Arial", 12, "bold"))
        create_trip_frame.pack(pady=10, padx=10, fill="both", expand=True)

        create_trip_frame.grid_columnconfigure(0, weight=1)
        create_trip_frame.grid_columnconfigure(1, weight=3)
        create_trip_frame.grid_columnconfigure(2, weight=1)

        Label(create_trip_frame, text="Destination", font=("Arial", 10, "bold"), fg="blue").grid(row=0, column=0, pady=5, sticky=W)
        self.destination_entry = Entry(create_trip_frame)
        self.destination_entry.grid(row=0, column=1, pady=5)

        Label(create_trip_frame, text="Start Date", font=("Arial", 10, "bold"), fg="blue").grid(row=1, column=0, pady=5, sticky=W)
        self.start_date_button = Button(create_trip_frame, text="Select Date", command=lambda: self.open_date_picker("start_date"), fg="black")
        self.start_date_button.grid(row=1, column=1, pady=5)

        Label(create_trip_frame, text="End Date", font=("Arial", 10, "bold"), fg="blue").grid(row=2, column=0, pady=5, sticky=W)
        self.end_date_button = Button(create_trip_frame, text="Select Date", command=lambda: self.open_date_picker("end_date"), fg="black")
        self.end_date_button.grid(row=2, column=1, pady=5)

        Label(create_trip_frame, text="Budget (€)", font=("Arial", 10, "bold"), fg="blue").grid(row=3, column=0, pady=5, sticky=W)
        self.budget_entry = Entry(create_trip_frame)
        self.budget_entry.grid(row=3, column=1, pady=5)

        create_trip_button = Button(create_trip_frame, text="Create Trip", font=("Arial", 10, "bold"), command=self.create_trip, fg="black")
        create_trip_button.grid(row=4, columnspan=3, pady=10)

        # Add Activity Section
        add_activity_frame = LabelFrame(self.root, text="Add Activity", font=("Arial", 12, "bold"))
        add_activity_frame.pack(pady=10, padx=10, fill="both", expand=True)

        Label(add_activity_frame, text="Activity Name", font=("Arial", 10, "bold"), fg="blue").grid(row=0, column=0, pady=5, sticky=W)
        self.activity_name_entry = Entry(add_activity_frame)
        self.activity_name_entry.grid(row=0, column=1, pady=5)

        Label(add_activity_frame, text="Type", font=("Arial", 10, "bold"), fg="blue").grid(row=1, column=0, pady=5, sticky=W)
        self.activity_type_entry = Entry(add_activity_frame)
        self.activity_type_entry.grid(row=1, column=1, pady=5)

        Label(add_activity_frame, text="Cost (€)", font=("Arial", 10, "bold"), fg="blue").grid(row=2, column=0, pady=5, sticky=W)
        self.activity_cost_entry = Entry(add_activity_frame)
        self.activity_cost_entry.grid(row=2, column=1, pady=5)

        Label(add_activity_frame, text="Time (HH:MM)", font=("Arial", 10, "bold"), fg="blue").grid(row=3, column=0, pady=5, sticky=W)
        self.activity_time_entry = Entry(add_activity_frame)
        self.activity_time_entry.grid(row=3, column=1, pady=5)

        time_buttons_frame = Frame(add_activity_frame)
        time_buttons_frame.grid(row=3, column=2, pady=5)

        self.hour_button = Button(time_buttons_frame, text="HH", command=self.select_hour)
        self.hour_button.grid(row=0, column=0, padx=5)

        self.minute_button = Button(time_buttons_frame, text="MM", command=self.select_minute)
        self.minute_button.grid(row=0, column=1, padx=5)

        Label(add_activity_frame, text="Goal", font=("Arial", 10, "bold"), fg="blue").grid(row=4, column=0, pady=5, sticky=W)
        self.activity_goal_entry = Entry(add_activity_frame)
        self.activity_goal_entry.grid(row=4, column=1, pady=5)

        add_activity_button = Button(add_activity_frame, text="Add Activity", font=("Arial", 10, "bold"), command=self.add_activity, fg="black")
        add_activity_button.grid(row=5, columnspan=2, pady=10)

        # Current Trip Details Section
        current_trip_frame = LabelFrame(self.root, text="Current Trip Details", font=("Arial", 12, "bold"))
        current_trip_frame.pack(pady=10, padx=10, fill="both", expand=True)

        current_trip_inner_frame = Frame(current_trip_frame)
        current_trip_inner_frame.pack(side=LEFT, fill="both", expand=True)

        # Navigation Buttons
        navigation_frame = Frame(current_trip_inner_frame)
        navigation_frame.pack(side=TOP, padx=10, pady=5)

        previous_button = Button(navigation_frame, text="Previous", font=("Arial", 10, "bold"), command=self.previous_trip, fg="black")
        previous_button.pack(side=LEFT, padx=5)

        next_button = Button(navigation_frame, text="Next", font=("Arial", 10, "bold"), command=self.next_trip, fg="black")
        next_button.pack(side=LEFT)

        self.trip_details_text = Text(current_trip_inner_frame, height=8, width=55)
        self.trip_details_text.pack(pady=10, padx=10, side=LEFT, fill=Y, expand=True)

        # Error Message Section
        error_frame = Frame(self.root)
        error_frame.pack(pady=5, padx=10, fill="x")

        error_label = Label(error_frame, text="Error Message", font=("Arial", 10, "bold"), fg="red")
        error_label.pack(side=LEFT)

        # display the error message
        self.error_label = Label(error_frame, textvariable=self.error_message, font=("Arial", 10), fg="red", width=50, anchor="w")
        self.error_label.pack(side=LEFT, padx=10)

        # select dates
        self.selected_dates = {"start_date": "", "end_date": ""}

    def select_hour(self):
        hour_popup = Toplevel(self.root)
        hour_popup.title("Select Hour")
        hour_popup.geometry("200x200")

        hours = [f"{i:02d}" for i in range(24)]
        hour_var = StringVar(hour_popup)
        hour_var.set(hours[0])  # Default value

        hour_menu = OptionMenu(hour_popup, hour_var, *hours)
        hour_menu.pack(pady=10)

        def set_hour():
            self.activity_time_entry.delete(0, END)
            self.activity_time_entry.insert(0, f"{hour_var.get()}:")
            hour_popup.destroy()

        select_button = Button(hour_popup, text="Select", command=set_hour)
        select_button.pack(pady=10)

    def select_minute(self):
        minute_popup = Toplevel(self.root)
        minute_popup.title("Select Minute")
        minute_popup.geometry("200x200")

        minutes = [f"{i:02d}" for i in range(60)]
        minute_var = StringVar(minute_popup)
        minute_var.set(minutes[0])  # Default value

        minute_menu = OptionMenu(minute_popup, minute_var, *minutes)
        minute_menu.pack(pady=10)

        def set_minute():
            self.activity_time_entry.delete(3, END)
            self.activity_time_entry.insert(3, minute_var.get())
            minute_popup.destroy()

        select_button = Button(minute_popup, text="Select", command=set_minute)
        select_button.pack(pady=10)

    def open_date_picker(self, field):
        date_picker = Toplevel(self.root)
        date_picker.title("Select Date")
        date_picker.geometry("250x250")

        Label(date_picker, text="Day", fg="blue").pack(pady=5)
        day_entry = Entry(date_picker)
        day_entry.pack(pady=5)

        Label(date_picker, text="Month", fg="blue").pack(pady=5)
        month_entry = Entry(date_picker)
        month_entry.pack(pady=5)

        Label(date_picker, text="Year", fg="blue").pack(pady=5)
        year_entry = Entry(date_picker)
        year_entry.pack(pady=5)

        def display_date():
            try:
                day, month, year = int(day_entry.get()), int(month_entry.get()), int(year_entry.get())
                formatted_date = f"{day:02d}/{month:02d}/{year}"
                self.selected_dates[field] = formatted_date
                if field == "start_date":
                    self.start_date_button.config(text=formatted_date)
                else:
                    self.end_date_button.config(text=formatted_date)
                date_picker.destroy()
            except ValueError:
                self.error_message.set("Invalid date format")

        select_button = Button(date_picker, text="Select", command=display_date)
        select_button.pack(pady=10)

    def create_trip(self):
        destination = self.destination_entry.get()
        budget = self.budget_entry.get()

        if destination and budget.isnumeric():
            trip = {"destination": destination, "budget": int(budget), "activities": []}
            self.trip_list.append(trip)
            self.current_trip_index = len(self.trip_list) - 1
            self.show_current_trip_details()
            self.clear_create_trip_fields()
            self.error_message.set("")  # Clear the error message when itsvalid
        else:
            self.error_message.set("Invalid input for destination or budget")

    def add_activity(self):
        # Get values from the activity fields
        activity_name = self.activity_name_entry.get().strip()
        activity_type = self.activity_type_entry.get().strip()
        activity_cost = self.activity_cost_entry.get().strip()
        activity_goal = self.activity_goal_entry.get().strip()
        activity_time = self.activity_time_entry.get().strip()

        # Clear error message
        self.error_message.set("")

        if activity_name and activity_type and activity_goal and activity_time:
            try:
                activity_cost = float(activity_cost)
                activity = {
                    "name": activity_name,
                    "type": activity_type,
                    "cost": activity_cost,
                    "time": activity_time,
                    "goal": activity_goal,
                }

                self.trip_list[self.current_trip_index]["activities"].append(activity)

                self.show_current_trip_details()

                self.clear_activity_fields()

            except ValueError:

                self.error_message.set("Invalid cost. Please enter a valid number.")
        else:

            self.error_message.set("All fields are required for activity.")

    def show_current_trip_details(self):
        # Fetch current trip details
        trip = self.trip_list[self.current_trip_index]

        # Start with basic trip info
        details = f"Destination: {trip['destination']}\n"
        details += f"Budget: €{trip['budget']}\n\n"

        # make sure the activities aare visible, if details given
        if trip["activities"]:
            details += "Activities:\n"
            for activity in trip["activities"]:
                details += (
                    f"  - {activity['name']} ({activity['type']})\n"
                    f"    Cost: €{activity['cost']} | Time: {activity['time']}\n"
                    f"    Goal: {activity['goal']}\n\n"
                )
        else:
            details += "No activities added yet.\n"

        # Update the trip details text box
        self.trip_details_text.delete(1.0, END)
        self.trip_details_text.insert(END, details)

    def clear_create_trip_fields(self):
        self.destination_entry.delete(0, END)
        self.budget_entry.delete(0, END)

    def clear_activity_fields(self):
        self.activity_name_entry.delete(0, END)
        self.activity_type_entry.delete(0, END)
        self.activity_cost_entry.delete(0, END)
        self.activity_goal_entry.delete(0, END)
        self.activity_time_entry.delete(0, END)

    def previous_trip(self):
        if self.current_trip_index > 0:
            self.current_trip_index -= 1
            self.show_current_trip_details()
        else:
            self.error_message.set("No previous trip available.")

    def next_trip(self):
        if self.current_trip_index < len(self.trip_list) - 1:
            self.current_trip_index += 1
            self.show_current_trip_details()
        else:
            self.error_message.set("No next trip available")

    def clear_all_if_checked(self):
        if self.clear_all_var.get():
            # Clear trip list and reset the trip
            self.trip_list.clear()
            self.trip_details_text.delete(1.0, END)

            # Clear all the fields in Create Trip section
            self.destination_entry.delete(0, END)
            self.budget_entry.delete(0, END)

            # Clear all fields in Add Activity section
            self.activity_name_entry.delete(0, END)
            self.activity_type_entry.delete(0, END)
            self.activity_cost_entry.delete(0, END)
            self.activity_goal_entry.delete(0, END)
            self.activity_time_entry.delete(0, END)

            # Clear the selected start and end date buttons
            self.start_date_button.config(text="Select Date")
            self.end_date_button.config(text="Select Date")

            # Reset the error message
            self.error_message.set("")

root = Tk()
app = TravelCompanionApp(root)
root.mainloop()