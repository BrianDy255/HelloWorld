def banner_text(text: str =" ",screen_width: int = 60) -> None:
    """
    Function creates a banner text using the `*` creating a properly
    formatted banner with center alignment.

    :param text: Enter a sentence or word to fill
    :param screen_width: an Integer to determine width of banner
    :return: None
    :raise Exception: ValueError if the string is larger than the
        specified width
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified"
                         "width {1}".format(text,screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f'**{text.center(screen_width-4)}**'
        print(output_string)

banner_text("*",60)
banner_text("Always look on the bright side of life",60)
banner_text("If life seems jolly rotten,",60)
banner_text("There's something you've forgotten",60)
banner_text(screen_width=60)
