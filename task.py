def tell_fortune(num_children, partner_name, location, job_title):
    fortune = f"""You will be a {job_title} in {location},
    and married to {partner_name} with {num_children} kids."""
    print(fortune)


# Calling the function with different values
tell_fortune(2, "John", "New York", "Software Engineer")
tell_fortune(0, "Alice", "London", "Graphic Designer")
tell_fortune(3, "Mike", "Los Angeles", "Teacher")
