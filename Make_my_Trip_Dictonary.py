Make_My_Trip = { 
    "Flight": ["One Way", "Round Trip", "Multi city"],
    "From": ["Mumbai city", "New Delhi", "Bangkok Thailand", "Pune India"],
    "To": ["Mumbai city", "New Delhi", "Bangkok Thailand", "Pune India"],
    "Departure": ["Sunday 1st September 2024"],
    "Return": ["2nd October 2024"],
    "Travel_Class": ["Adults 12+"],
    "Hotel": ["Various hotels, homestays, and villas"],
    "Holiday_Packages": ["Customized holiday packages"],
    "Trains": ["Train ticket bookings"],
    "Buses": ["Bus ticket bookings"],
    "Cabs": ["Inter-city and local cab services"],
    "Forex": ["Forex card and currency exchange"],
    "Travel_Insurance": ["Various travel insurance options"],
    "Activities": ["Booking activities and experiences"]
}
for key, value in Make_My_Trip.items():
    if key == "Flight":
        print(f"{key}: {value}", end=", ")
    else:
        print(f"{key}: {value}")

