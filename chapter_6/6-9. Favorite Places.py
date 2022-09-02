favorite_places={
    "jack": ' home , beach , see ',
    "mike": ' bed , doha , his desk ',
    "david": ' school , beach , playground  '
}
for names, places in favorite_places.items():
    if names == "jack":
        print(f"Your favorite places MS.Jack are::\n{places}")
        print("")
    elif names == "mike":
        print(f"Your favorite places MS.Mike are::\n{places}")
        print("")
    else:
        print(f"Your favorite places MS.David are::\n{places}")
        print("")
